"""
LSM-Tree 学习指南和进阶示例

这个文件提供了LSM-Tree的详细学习指南，包括：
1. 核心概念解释
2. 实现细节分析
3. 性能优化技巧
4. 实际应用场景
5. 进阶功能演示
"""

import time
import random
import threading
from lsm_tree import LSMTree, MemTable, SSTable


class LSMTreeGuide:
    """LSM-Tree学习指南类"""
    
    def __init__(self):
        self.examples = []
    
    def explain_core_concepts(self):
        """解释LSM-Tree核心概念"""
        print("=" * 60)
        print("LSM-Tree 核心概念解释")
        print("=" * 60)
        
        concepts = {
            "1. 什么是LSM-Tree": """
            LSM-Tree (Log-Structured Merge-Tree) 是一种数据结构，专门用于处理大量写入操作。
            
            核心思想：
            - 将随机写入转换为顺序写入，提高磁盘I/O效率
            - 使用多层存储结构，内存中快速写入，磁盘中持久化存储
            - 通过合并(Compaction)操作减少读取时的查找次数
            """,
            
            "2. 主要组件": """
            MemTable (内存表):
            - 位于内存中的有序数据结构
            - 用于快速处理写入操作
            - 当达到容量限制时，会flush到磁盘
            
            SSTable (Sorted String Table):
            - 磁盘上的不可变有序表
            - 数据按key排序存储
            - 支持高效的顺序读取
            
            Compaction (合并):
            - 将多个小的SSTable合并成大的SSTable
            - 减少读取时需要查找的文件数量
            - 删除过期的数据
            """,
            
            "3. 写入流程": """
            1. 数据首先写入MemTable（内存，快速）
            2. 当MemTable满时，flush到Level 0的SSTable
            3. 当Level N的SSTable数量超过阈值时，触发Compaction
            4. Compaction将Level N的数据合并到Level N+1
            """,
            
            "4. 读取流程": """
            1. 首先在MemTable中查找
            2. 如果没找到，按层级从新到旧查找SSTable
            3. 可以使用Bloom Filter快速判断键是否存在
            4. 找到第一个匹配的键值对就返回（最新值）
            """,
            
            "5. 优势与劣势": """
            优势：
            - 极高的写入性能（顺序写入）
            - 良好的压缩比
            - 支持范围查询
            
            劣势：
            - 读取性能相对较低（可能需要查找多个文件）
            - 需要额外的Compaction开销
            - 空间放大（同一数据可能存在于多个层级）
            """
        }
        
        for title, content in concepts.items():
            print(f"\n{title}")
            print("-" * 40)
            print(content)
    
    def demonstrate_write_amplification(self):
        """演示写入放大现象"""
        print("\n" + "=" * 60)
        print("写入放大 (Write Amplification) 演示")
        print("=" * 60)
        
        lsm = LSMTree(data_dir="./write_amp_demo", max_memtable_size=3)
        
        print("插入6个键值对，观察MemTable flush和Compaction:")
        keys = [f"key_{i}" for i in range(6)]
        
        for i, key in enumerate(keys):
            lsm.put(key, f"value_{i}")
            print(f"插入 {key} -> MemTable大小: {lsm.memtable.size}")
            
            # 显示SSTable状态
            stats = lsm.get_stats()
            for level_stat in stats['levels']:
                if level_stat['sstable_count'] > 0:
                    print(f"  Level {level_stat['level']}: {level_stat['sstable_count']} SSTables")
    
    def demonstrate_read_performance(self):
        """演示读取性能特点"""
        print("\n" + "=" * 60)
        print("读取性能演示")
        print("=" * 60)
        
        lsm = LSMTree(data_dir="./read_perf_demo", max_memtable_size=50)
        
        # 插入大量数据
        print("插入1000个键值对...")
        for i in range(1000):
            lsm.put(f"key_{i:04d}", f"value_{i:04d}")
        
        # 测试不同场景的读取性能
        scenarios = [
            ("最近写入的数据", [f"key_{i:04d}" for i in range(950, 1000)]),
            ("较早写入的数据", [f"key_{i:04d}" for i in range(0, 50)]),
            ("随机访问", [f"key_{random.randint(0, 999):04d}" for _ in range(50)])
        ]
        
        for scenario_name, keys in scenarios:
            start_time = time.time()
            for key in keys:
                value = lsm.get(key)
            end_time = time.time()
            
            print(f"{scenario_name}: {len(keys)}次读取耗时 {end_time - start_time:.4f}秒")
    
    def demonstrate_compaction_impact(self):
        """演示Compaction对性能的影响"""
        print("\n" + "=" * 60)
        print("Compaction影响演示")
        print("=" * 60)
        
        lsm = LSMTree(data_dir="./compaction_demo", max_memtable_size=10)
        
        print("逐步插入数据，观察Compaction触发:")
        
        for batch in range(5):
            print(f"\n批次 {batch + 1}: 插入20个键值对")
            start_time = time.time()
            
            for i in range(20):
                key = f"batch_{batch}_key_{i:02d}"
                lsm.put(key, f"batch_{batch}_value_{i:02d}")
            
            end_time = time.time()
            
            # 显示当前状态
            stats = lsm.get_stats()
            print(f"  插入耗时: {end_time - start_time:.4f}秒")
            print(f"  MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
            
            for level_stat in stats['levels']:
                if level_stat['sstable_count'] > 0:
                    print(f"  Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")
    
    def demonstrate_concurrent_access(self):
        """演示并发访问"""
        print("\n" + "=" * 60)
        print("并发访问演示")
        print("=" * 60)
        
        lsm = LSMTree(data_dir="./concurrent_demo", max_memtable_size=100)
        
        def writer_thread(thread_id, num_writes):
            """写入线程"""
            for i in range(num_writes):
                key = f"thread_{thread_id}_key_{i:03d}"
                lsm.put(key, f"thread_{thread_id}_value_{i:03d}")
        
        def reader_thread(thread_id, num_reads):
            """读取线程"""
            for i in range(num_reads):
                key = f"thread_{thread_id}_key_{i:03d}"
                value = lsm.get(key)
        
        # 创建多个线程
        threads = []
        
        # 写入线程
        for i in range(3):
            t = threading.Thread(target=writer_thread, args=(i, 50))
            threads.append(t)
        
        # 读取线程
        for i in range(2):
            t = threading.Thread(target=reader_thread, args=(i, 50))
            threads.append(t)
        
        # 启动所有线程
        start_time = time.time()
        for t in threads:
            t.start()
        
        # 等待所有线程完成
        for t in threads:
            t.join()
        
        end_time = time.time()
        
        print(f"并发测试完成，总耗时: {end_time - start_time:.4f}秒")
        
        # 显示最终状态
        stats = lsm.get_stats()
        print(f"最终MemTable大小: {stats['memtable_size']}")
        for level_stat in stats['levels']:
            if level_stat['sstable_count'] > 0:
                print(f"Level {level_stat['level']}: {level_stat['sstable_count']} SSTables")
    
    def demonstrate_space_efficiency(self):
        """演示空间效率"""
        print("\n" + "=" * 60)
        print("空间效率演示")
        print("=" * 60)
        
        lsm = LSMTree(data_dir="./space_demo", max_memtable_size=20)
        
        # 插入重复键，观察空间使用
        print("插入重复键，观察空间放大:")
        
        for round_num in range(3):
            print(f"\n第 {round_num + 1} 轮:")
            for i in range(10):
                key = f"common_key_{i}"
                value = f"round_{round_num}_value_{i}"
                lsm.put(key, value)
            
            stats = lsm.get_stats()
            total_keys = sum(level_stat['total_keys'] for level_stat in stats['levels'])
            print(f"  总键数: {total_keys} (实际唯一键: 10)")
            print(f"  空间放大比: {total_keys / 10:.1f}x")
    
    def demonstrate_range_queries(self):
        """演示范围查询"""
        print("\n" + "=" * 60)
        print("范围查询演示")
        print("=" * 60)
        
        lsm = LSMTree(data_dir="./range_demo", max_memtable_size=50)
        
        # 插入有序数据
        print("插入有序数据...")
        for i in range(100):
            lsm.put(f"key_{i:03d}", f"value_{i:03d}")
        
        # 实现简单的范围查询
        def range_query(start_key, end_key):
            """简单的范围查询实现"""
            results = []
            
            # 在MemTable中查找
            for key, value in lsm.memtable.data.items():
                if start_key <= key <= end_key:
                    results.append((key, value))
            
            # 在SSTables中查找
            for level in range(len(lsm.sstables)):
                for sstable in reversed(lsm.sstables[level]):
                    for key, value in sstable.data.items():
                        if start_key <= key <= end_key:
                            results.append((key, value))
            
            # 去重并排序
            unique_results = {}
            for key, value in results:
                if key not in unique_results:
                    unique_results[key] = value
            
            return sorted(unique_results.items())
        
        # 测试范围查询
        queries = [
            ("key_010", "key_020"),
            ("key_050", "key_070"),
            ("key_090", "key_099")
        ]
        
        for start, end in queries:
            results = range_query(start, end)
            print(f"范围查询 [{start}, {end}]: 找到 {len(results)} 个结果")
            for key, value in results[:3]:  # 只显示前3个
                print(f"  {key} -> {value}")
            if len(results) > 3:
                print(f"  ... 还有 {len(results) - 3} 个结果")
    
    def run_all_demos(self):
        """运行所有演示"""
        self.explain_core_concepts()
        self.demonstrate_write_amplification()
        self.demonstrate_read_performance()
        self.demonstrate_compaction_impact()
        self.demonstrate_concurrent_access()
        self.demonstrate_space_efficiency()
        self.demonstrate_range_queries()
        
        print("\n" + "=" * 60)
        print("LSM-Tree 学习指南完成！")
        print("=" * 60)
        print("""
        总结：
        1. LSM-Tree通过将随机写入转换为顺序写入，实现了极高的写入性能
        2. 多层存储结构平衡了内存和磁盘的使用
        3. Compaction机制保证了读取性能，但会带来额外的写入开销
        4. 适合写多读少的场景，如日志系统、时序数据库等
        
        实际应用：
        - LevelDB / RocksDB: Google/Facebook开发的键值存储引擎
        - Cassandra: 分布式NoSQL数据库
        - InfluxDB: 时序数据库
        - Apache Kafka: 消息队列系统
        """)


if __name__ == "__main__":
    guide = LSMTreeGuide()
    guide.run_all_demos()
