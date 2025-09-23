"""
LSM-Tree V2 - 支持多种存储后端

这个版本重构了LSM-Tree，使用存储抽象接口，支持：
- Pickle文件存储
- JSON文件存储  
- Excel文件存储
- S3网络存储
- 内存存储
"""

import os
import time
import threading
from typing import Optional, List, Tuple, Dict, Any
from collections import OrderedDict
from storage_interface import StorageBackend, StorageFactory


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
    """SSTable - 使用存储后端的有序字符串表"""
    
    def __init__(self, storage: StorageBackend, sstable_key: str, level: int = 0):
        self.storage = storage
        self.sstable_key = sstable_key
        self.level = level
        self.data = OrderedDict()
        self.min_key = None
        self.max_key = None
        self._load_data()
    
    def _load_data(self):
        """从存储后端加载数据"""
        try:
            data = self.storage.read(self.sstable_key)
            if data:
                self.data = OrderedDict(data)
                if self.data:
                    keys = list(self.data.keys())
                    self.min_key = keys[0]
                    self.max_key = keys[-1]
        except Exception as e:
            print(f"加载SSTable失败: {e}")
            self.data = OrderedDict()
    
    def write_data(self, data: List[Tuple[str, str]]):
        """将数据写入存储后端"""
        # 确保数据按key排序
        data.sort(key=lambda x: x[0])
        
        for key, value in data:
            self.data[key] = value
        
        if self.data:
            keys = list(self.data.keys())
            self.min_key = keys[0]
            self.max_key = keys[-1]
        
        # 写入存储后端
        try:
            self.storage.write(self.sstable_key, dict(self.data))
        except Exception as e:
            print(f"写入SSTable失败: {e}")
    
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
    
    def delete(self):
        """删除SSTable"""
        try:
            self.storage.delete(self.sstable_key)
        except Exception as e:
            print(f"删除SSTable失败: {e}")


class BloomFilter:
    """简单的布隆过滤器实现"""
    
    def __init__(self, capacity: int = 1000, error_rate: float = 0.01):
        import math
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


class LSMTreeV2:
    """LSM-Tree V2 - 支持多种存储后端"""
    
    def __init__(self, storage_type: str = 'pickle', storage_config: Dict[str, Any] = None, 
                 max_memtable_size: int = 1000):
        self.storage_type = storage_type
        self.storage_config = storage_config or {}
        self.max_memtable_size = max_memtable_size
        
        # 创建存储后端
        self.storage = StorageFactory.create_storage(storage_type, storage_config)
        
        # LSM-Tree组件
        self.memtable = MemTable(max_memtable_size)
        self.sstables = []  # List[List[SSTable]] - 每层一个列表
        self.max_levels = 7
        self.level_capacity = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
        self.lock = threading.RLock()
        
        # 加载现有的SSTables
        self._load_existing_sstables()
    
    def _load_existing_sstables(self):
        """加载现有的SSTables"""
        self.sstables = [[] for _ in range(self.max_levels)]
        
        try:
            # 从存储后端获取所有键
            all_keys = self.storage.list_keys()
            
            for key in all_keys:
                # 解析键格式: level_X_timestamp
                if key.startswith('level_'):
                    parts = key.split('_')
                    if len(parts) >= 3:
                        try:
                            level = int(parts[1])
                            if 0 <= level < self.max_levels:
                                sstable = SSTable(self.storage, key, level)
                                self.sstables[level].append(sstable)
                        except ValueError:
                            continue
        except Exception as e:
            print(f"加载现有SSTables失败: {e}")
    
    def put(self, key: str, value: str):
        """插入键值对"""
        with self.lock:
            # 写入MemTable
            if self.memtable.put(key, value):
                # MemTable满了，需要flush到存储后端
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
        """将MemTable刷新到存储后端"""
        if not self.memtable.data:
            return
        
        # 创建新的SSTable
        timestamp = int(time.time() * 1000000)  # 微秒时间戳
        level = 0
        sstable_key = f"level_{level}_{timestamp}"
        
        # 写入数据
        sstable = SSTable(self.storage, sstable_key, level)
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
        sstable_key = f"level_{next_level}_{timestamp}"
        
        new_sstable = SSTable(self.storage, sstable_key, next_level)
        new_sstable.write_data(list(merged_data.items()))
        
        # 更新SSTables列表
        self.sstables[next_level].append(new_sstable)
        
        # 删除旧的SSTables
        for sstable in current_level_sstables:
            sstable.delete()
        
        self.sstables[level] = []
        
        # 递归检查下一层是否需要compaction
        self._check_compaction()
    
    def get_stats(self) -> Dict[str, Any]:
        """获取LSM-Tree统计信息"""
        stats = {
            "storage_type": self.storage_type,
            "storage_config": self.storage_config,
            "memtable_size": self.memtable.size,
            "memtable_max_size": self.memtable.max_size,
            "levels": [],
            "storage_stats": self.storage.get_stats()
        }
        
        for level, sstables in enumerate(self.sstables):
            level_stats = {
                "level": level,
                "sstable_count": len(sstables),
                "total_keys": sum(sstable.size() for sstable in sstables)
            }
            stats["levels"].append(level_stats)
        
        return stats
    
    def switch_storage(self, new_storage_type: str, new_storage_config: Dict[str, Any] = None):
        """切换存储后端"""
        with self.lock:
            # 创建新的存储后端
            new_storage = StorageFactory.create_storage(new_storage_type, new_storage_config or {})
            
            # 迁移所有SSTables
            for level in range(len(self.sstables)):
                for sstable in self.sstables[level]:
                    # 读取数据
                    data = dict(sstable.data)
                    # 写入新存储后端
                    new_storage.write(sstable.sstable_key, data)
                    # 删除旧数据
                    sstable.delete()
            
            # 更新存储后端
            self.storage = new_storage
            self.storage_type = new_storage_type
            self.storage_config = new_storage_config or {}
            
            print(f"存储后端已切换到: {new_storage_type}")


# 测试和演示代码
def test_lsm_tree_v2():
    """测试LSM-Tree V2功能"""
    print("=== LSM-Tree V2 测试开始 ===")
    
    # 测试不同存储后端
    storage_types = ['pickle', 'json', 'memory']
    
    for storage_type in storage_types:
        print(f"\n--- 测试 {storage_type.upper()} 存储后端 ---")
        
        # 创建LSM-Tree实例
        config = {'base_path': f'../data/test_{storage_type}_data'}
        lsm = LSMTreeV2(storage_type=storage_type, storage_config=config, max_memtable_size=3)
        
        # 测试基本操作
        test_data = [
            ("key1", "value1"),
            ("key2", "value2"),
            ("key3", "value3"),
            ("key4", "value4"),  # 这会触发MemTable flush
        ]
        
        print("插入测试数据:")
        for key, value in test_data:
            lsm.put(key, value)
            print(f"  插入: {key} -> {value}")
        
        print("读取测试:")
        for key, expected_value in test_data:
            actual_value = lsm.get(key)
            print(f"  读取 {key}: {actual_value} (期望: {expected_value})")
            assert actual_value == expected_value, f"读取失败: {key}"
        
        # 显示统计信息
        stats = lsm.get_stats()
        print(f"统计信息: {stats}")
    
    print("\n=== LSM-Tree V2 测试完成 ===")


def demo_storage_switching():
    """演示存储后端切换"""
    print("\n=== 存储后端切换演示 ===")
    
    # 从内存存储开始
    lsm = LSMTreeV2(storage_type='memory', max_memtable_size=5)
    
    # 插入一些数据
    print("1. 在内存存储中插入数据")
    for i in range(8):
        key = f"key_{i}"
        value = f"value_{i}"
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    # 显示内存存储状态
    stats = lsm.get_stats()
    print(f"内存存储状态: {stats}")
    
    # 切换到JSON存储
    print("\n2. 切换到JSON存储")
    lsm.switch_storage('json', {'base_path': './switched_data'})
    
    # 验证数据迁移
    print("验证数据迁移:")
    for i in range(8):
        key = f"key_{i}"
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    # 显示JSON存储状态
    stats = lsm.get_stats()
    print(f"JSON存储状态: {stats}")
    
    print("\n=== 存储后端切换演示完成 ===")


if __name__ == "__main__":
    # 运行测试
    test_lsm_tree_v2()
    
    # 运行存储切换演示
    demo_storage_switching()
