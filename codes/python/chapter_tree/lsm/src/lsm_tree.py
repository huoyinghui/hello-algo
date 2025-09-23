"""
LSM-Tree (Log-Structured Merge-Tree) 实现

LSM-Tree是一种用于处理大量写入操作的数据结构，广泛应用于现代数据库系统如LevelDB、RocksDB等。
它的核心思想是将随机写入转换为顺序写入，通过多层存储结构实现高效的读写操作。

主要组件：
1. MemTable: 内存中的有序表，用于快速写入
2. SSTable: 磁盘上的有序表，不可变
3. Compaction: 合并策略，减少读取时的查找次数
4. Bloom Filter: 快速判断键是否存在，减少不必要的磁盘读取
"""

import os
import json
import pickle
import threading
from typing import Optional, List, Tuple, Dict, Any
from collections import OrderedDict
import time


class MemTable:
    """内存表 - LSM-Tree的内存组件"""
    
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self.data = OrderedDict()  # 保持插入顺序的有序字典
        self.size = 0
        
    def put(self, key: str, value: str) -> bool:
        """插入键值对"""
        if key not in self.data:
            self.size += 1
        self.data[key] = value
        return self.size >= self.max_size
    
    def get(self, key: str) -> Optional[str]:
        """获取值"""
        return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        """删除键（标记删除）"""
        if key in self.data:
            self.data[key] = None  # 标记删除
            return True
        return False
    
    def is_full(self) -> bool:
        """检查是否已满"""
        return self.size >= self.max_size
    
    def get_sorted_data(self) -> List[Tuple[str, str]]:
        """获取排序后的数据，用于写入SSTable"""
        return [(k, v) for k, v in self.data.items() if v is not None]


class SSTable:
    """SSTable - 磁盘上的有序字符串表"""
    
    def __init__(self, file_path: str, level: int = 0):
        self.file_path = file_path
        self.level = level
        self.data = OrderedDict()
        self.min_key = None
        self.max_key = None
        self._load_data()
    
    def _load_data(self):
        """从文件加载数据"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'rb') as f:
                    self.data = pickle.load(f)
                if self.data:
                    keys = list(self.data.keys())
                    self.min_key = keys[0]
                    self.max_key = keys[-1]
            except Exception as e:
                print(f"加载SSTable失败: {e}")
                self.data = OrderedDict()
    
    def write_data(self, data: List[Tuple[str, str]]):
        """将数据写入SSTable"""
        # 确保数据按key排序
        data.sort(key=lambda x: x[0])
        
        for key, value in data:
            self.data[key] = value
        
        if self.data:
            keys = list(self.data.keys())
            self.min_key = keys[0]
            self.max_key = keys[-1]
        
        # 写入文件
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.data, f)
    
    def get(self, key: str) -> Optional[str]:
        """获取值"""
        return self.data.get(key)
    
    def contains_key(self, key: str) -> bool:
        """检查是否包含键"""
        return key in self.data
    
    def get_key_range(self) -> Tuple[Optional[str], Optional[str]]:
        """获取键的范围"""
        return self.min_key, self.max_key
    
    def size(self) -> int:
        """获取大小"""
        return len(self.data)


class BloomFilter:
    """简单的布隆过滤器实现"""
    
    def __init__(self, capacity: int = 1000, error_rate: float = 0.01):
        self.capacity = capacity
        self.error_rate = error_rate
        self.bit_array_size = int(-(capacity * math.log(error_rate)) / (math.log(2) ** 2))
        self.hash_count = int((self.bit_array_size / capacity) * math.log(2))
        self.bit_array = [False] * self.bit_array_size
    
    def _hash(self, item: str, seed: int) -> int:
        """简单的哈希函数"""
        hash_val = 0
        for char in item:
            hash_val = (hash_val * 31 + ord(char)) % self.bit_array_size
        return (hash_val + seed) % self.bit_array_size
    
    def add(self, item: str):
        """添加元素"""
        for i in range(self.hash_count):
            index = self._hash(item, i)
            self.bit_array[index] = True
    
    def might_contain(self, item: str) -> bool:
        """检查元素是否可能存在"""
        for i in range(self.hash_count):
            index = self._hash(item, i)
            if not self.bit_array[index]:
                return False
        return True


class LSMTree:
    """LSM-Tree主类"""
    
    def __init__(self, data_dir: str = "./lsm_data", max_memtable_size: int = 1000):
        self.data_dir = data_dir
        self.max_memtable_size = max_memtable_size
        self.memtable = MemTable(max_memtable_size)
        self.sstables = []  # List[List[SSTable]] - 每层一个列表
        self.max_levels = 7
        self.level_capacity = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
        self.lock = threading.RLock()
        
        # 初始化存储目录
        os.makedirs(data_dir, exist_ok=True)
        
        # 加载现有的SSTables
        self._load_existing_sstables()
    
    def _load_existing_sstables(self):
        """加载现有的SSTables"""
        self.sstables = [[] for _ in range(self.max_levels)]
        
        for level in range(self.max_levels):
            level_dir = os.path.join(self.data_dir, f"level_{level}")
            if os.path.exists(level_dir):
                for filename in os.listdir(level_dir):
                    if filename.endswith('.sst'):
                        file_path = os.path.join(level_dir, filename)
                        sstable = SSTable(file_path, level)
                        self.sstables[level].append(sstable)
    
    def put(self, key: str, value: str):
        """插入键值对"""
        with self.lock:
            # 写入MemTable
            if self.memtable.put(key, value):
                # MemTable满了，需要flush到磁盘
                self._flush_memtable()
    
    def get(self, key: str) -> Optional[str]:
        """获取值"""
        with self.lock:
            # 首先在MemTable中查找
            value = self.memtable.get(key)
            if value is not None:
                return value
            
            # 在SSTables中查找（从最新到最旧）
            for level in range(len(self.sstables)):
                for sstable in reversed(self.sstables[level]):
                    value = sstable.get(key)
                    if value is not None:
                        return value
            
            return None
    
    def delete(self, key: str) -> bool:
        """删除键"""
        with self.lock:
            # 在MemTable中标记删除
            return self.memtable.delete(key)
    
    def _flush_memtable(self):
        """将MemTable刷新到磁盘"""
        if not self.memtable.data:
            return
        
        # 创建新的SSTable
        timestamp = int(time.time() * 1000000)  # 微秒时间戳
        level = 0
        file_path = os.path.join(self.data_dir, f"level_{level}", f"{timestamp}.sst")
        
        # 写入数据
        sstable = SSTable(file_path, level)
        sstable.write_data(self.memtable.get_sorted_data())
        
        # 添加到SSTables列表
        self.sstables[level].append(sstable)
        
        # 清空MemTable
        self.memtable = MemTable(self.max_memtable_size)
        
        # 检查是否需要compaction
        self._check_compaction()
    
    def _check_compaction(self):
        """检查是否需要compaction"""
        for level in range(self.max_levels - 1):
            if len(self.sstables[level]) > self.level_capacity[level]:
                self._compact_level(level)
                break
    
    def _compact_level(self, level: int):
        """合并指定层的SSTables"""
        if level >= len(self.sstables) - 1:
            return
        
        current_level_sstables = self.sstables[level]
        if not current_level_sstables:
            return
        
        # 收集所有需要合并的数据
        all_data = []
        for sstable in current_level_sstables:
            for key, value in sstable.data.items():
                all_data.append((key, value))
        
        # 按key排序并去重（保留最新的值）
        all_data.sort(key=lambda x: x[0])
        merged_data = OrderedDict()
        for key, value in all_data:
            merged_data[key] = value
        
        # 创建新的SSTable到下一层
        timestamp = int(time.time() * 1000000)
        next_level = level + 1
        file_path = os.path.join(self.data_dir, f"level_{next_level}", f"{timestamp}.sst")
        
        new_sstable = SSTable(file_path, next_level)
        new_sstable.write_data(list(merged_data.items()))
        
        # 更新SSTables列表
        self.sstables[next_level].append(new_sstable)
        
        # 删除旧的SSTables
        for sstable in current_level_sstables:
            if os.path.exists(sstable.file_path):
                os.remove(sstable.file_path)
        
        self.sstables[level] = []
        
        # 递归检查下一层是否需要compaction
        self._check_compaction()
    
    def get_stats(self) -> Dict[str, Any]:
        """获取LSM-Tree统计信息"""
        stats = {
            "memtable_size": self.memtable.size,
            "memtable_max_size": self.memtable.max_size,
            "levels": []
        }
        
        for level, sstables in enumerate(self.sstables):
            level_stats = {
                "level": level,
                "sstable_count": len(sstables),
                "total_keys": sum(sstable.size() for sstable in sstables)
            }
            stats["levels"].append(level_stats)
        
        return stats


# 测试和演示代码
def test_lsm_tree():
    """测试LSM-Tree功能"""
    print("=== LSM-Tree 测试开始 ===")
    
    # 创建LSM-Tree实例
    lsm = LSMTree(data_dir="./test_lsm_data", max_memtable_size=5)
    
    # 测试基本操作
    print("\n1. 测试基本插入操作")
    test_data = [
        ("key1", "value1"),
        ("key2", "value2"),
        ("key3", "value3"),
        ("key4", "value4"),
        ("key5", "value5"),
        ("key6", "value6"),  # 这会触发MemTable flush
    ]
    
    for key, value in test_data:
        lsm.put(key, value)
        print(f"插入: {key} -> {value}")
    
    print(f"\nMemTable状态: {lsm.memtable.size}/{lsm.memtable.max_size}")
    
    # 测试读取操作
    print("\n2. 测试读取操作")
    for key, expected_value in test_data:
        actual_value = lsm.get(key)
        print(f"读取 {key}: {actual_value} (期望: {expected_value})")
        assert actual_value == expected_value, f"读取失败: {key}"
    
    # 测试不存在的键
    print("\n3. 测试不存在的键")
    non_existent = lsm.get("non_existent_key")
    print(f"不存在的键: {non_existent}")
    assert non_existent is None, "不存在的键应该返回None"
    
    # 测试删除操作
    print("\n4. 测试删除操作")
    lsm.delete("key2")
    deleted_value = lsm.get("key2")
    print(f"删除key2后读取: {deleted_value}")
    
    # 显示统计信息
    print("\n5. LSM-Tree统计信息")
    stats = lsm.get_stats()
    print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
    for level_stat in stats['levels']:
        if level_stat['sstable_count'] > 0:
            print(f"Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")
    
    print("\n=== LSM-Tree 测试完成 ===")


def demo_performance():
    """性能演示"""
    print("\n=== LSM-Tree 性能演示 ===")
    
    lsm = LSMTree(data_dir="./perf_lsm_data", max_memtable_size=100)
    
    # 批量写入测试
    print("\n1. 批量写入测试 (1000个键值对)")
    start_time = time.time()
    
    for i in range(1000):
        lsm.put(f"key_{i:04d}", f"value_{i:04d}")
    
    write_time = time.time() - start_time
    print(f"写入1000个键值对耗时: {write_time:.4f}秒")
    print(f"平均写入速度: {1000/write_time:.0f} ops/sec")
    
    # 批量读取测试
    print("\n2. 批量读取测试")
    start_time = time.time()
    
    for i in range(1000):
        value = lsm.get(f"key_{i:04d}")
        assert value == f"value_{i:04d}", f"读取失败: key_{i:04d}"
    
    read_time = time.time() - start_time
    print(f"读取1000个键值对耗时: {read_time:.4f}秒")
    print(f"平均读取速度: {1000/read_time:.0f} ops/sec")
    
    # 显示最终统计
    stats = lsm.get_stats()
    print(f"\n3. 最终统计信息")
    print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
    for level_stat in stats['levels']:
        if level_stat['sstable_count'] > 0:
            print(f"Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")
    
    print("\n=== 性能演示完成 ===")


if __name__ == "__main__":
    import math  # 为BloomFilter导入math模块
    
    # 运行测试
    test_lsm_tree()
    
    # 运行性能演示
    demo_performance()
