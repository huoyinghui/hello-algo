"""
LSM-Tree 可视化工具

这个工具可以帮助你直观地理解LSM-Tree的工作原理，
包括MemTable flush、Compaction过程等。
"""

import time
import os
from lsm_tree import LSMTree


class LSMTreeVisualizer:
    """LSM-Tree可视化器"""
    
    def __init__(self):
        self.lsm = None
    
    def visualize_memtable_flush(self):
        """可视化MemTable flush过程"""
        print("=" * 60)
        print("MemTable Flush 过程可视化")
        print("=" * 60)
        
        # 创建小容量的LSM-Tree以便观察flush
        self.lsm = LSMTree(data_dir="./visual_demo", max_memtable_size=3)
        
        print("MemTable容量限制: 3")
        print("插入数据观察flush过程:\n")
        
        for i in range(8):
            key = f"key_{i}"
            value = f"value_{i}"
            
            print(f"插入: {key} -> {value}")
            self.lsm.put(key, value)
            
            # 显示当前状态
            print(f"  MemTable状态: {self.lsm.memtable.size}/{self.lsm.memtable.max_size}")
            print(f"  MemTable内容: {dict(self.lsm.memtable.data)}")
            
            # 显示SSTable状态
            stats = self.lsm.get_stats()
            for level_stat in stats['levels']:
                if level_stat['sstable_count'] > 0:
                    print(f"  Level {level_stat['level']}: {level_stat['sstable_count']} SSTables")
            
            print()
    
    def visualize_compaction(self):
        """可视化Compaction过程"""
        print("=" * 60)
        print("Compaction 过程可视化")
        print("=" * 60)
        
        # 创建更小的容量限制以便快速触发compaction
        self.lsm = LSMTree(data_dir="./compaction_visual", max_memtable_size=2)
        
        print("MemTable容量限制: 2")
        print("Level 0容量限制: 3")
        print("插入数据观察Compaction:\n")
        
        for batch in range(4):
            print(f"--- 批次 {batch + 1} ---")
            
            for i in range(3):
                key = f"batch_{batch}_key_{i}"
                value = f"batch_{batch}_value_{i}"
                
                print(f"插入: {key} -> {value}")
                self.lsm.put(key, value)
            
            # 显示当前状态
            stats = self.lsm.get_stats()
            print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
            
            for level_stat in stats['levels']:
                if level_stat['sstable_count'] > 0:
                    print(f"Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")
            
            print()
    
    def visualize_read_process(self):
        """可视化读取过程"""
        print("=" * 60)
        print("读取过程可视化")
        print("=" * 60)
        
        self.lsm = LSMTree(data_dir="./read_visual", max_memtable_size=3)
        
        # 插入一些数据
        print("插入测试数据:")
        test_data = [
            ("key_1", "value_1"),
            ("key_2", "value_2"),
            ("key_3", "value_3"),
            ("key_4", "value_4"),
            ("key_5", "value_5"),
        ]
        
        for key, value in test_data:
            self.lsm.put(key, value)
            print(f"  {key} -> {value}")
        
        print(f"\n当前状态:")
        stats = self.lsm.get_stats()
        print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
        for level_stat in stats['levels']:
            if level_stat['sstable_count'] > 0:
                print(f"Level {level_stat['level']}: {level_stat['sstable_count']} SSTables")
        
        # 演示读取过程
        print(f"\n读取过程演示:")
        read_keys = ["key_1", "key_3", "key_5", "non_existent"]
        
        for key in read_keys:
            print(f"\n查找键: {key}")
            
            # 1. 在MemTable中查找
            memtable_value = self.lsm.memtable.get(key)
            if memtable_value is not None:
                print(f"  ✓ 在MemTable中找到: {memtable_value}")
                continue
            else:
                print(f"  ✗ MemTable中未找到")
            
            # 2. 在SSTables中查找
            found = False
            for level in range(len(self.lsm.sstables)):
                for sstable in reversed(self.lsm.sstables[level]):
                    sstable_value = sstable.get(key)
                    if sstable_value is not None:
                        print(f"  ✓ 在Level {level}的SSTable中找到: {sstable_value}")
                        found = True
                        break
                if found:
                    break
            
            if not found:
                print(f"  ✗ 在所有SSTables中都未找到")
    
    def visualize_space_usage(self):
        """可视化空间使用情况"""
        print("=" * 60)
        print("空间使用情况可视化")
        print("=" * 60)
        
        self.lsm = LSMTree(data_dir="./space_visual", max_memtable_size=5)
        
        print("插入重复键观察空间放大:\n")
        
        # 插入重复键
        for round_num in range(3):
            print(f"第 {round_num + 1} 轮插入:")
            
            for i in range(5):
                key = f"common_key_{i}"
                value = f"round_{round_num}_value_{i}"
                self.lsm.put(key, value)
                print(f"  {key} -> {value}")
            
            # 显示空间使用
            stats = self.lsm.get_stats()
            total_keys = sum(level_stat['total_keys'] for level_stat in stats['levels'])
            unique_keys = 5  # 实际唯一键数
            
            print(f"  总键数: {total_keys}")
            print(f"  唯一键数: {unique_keys}")
            print(f"  空间放大比: {total_keys / unique_keys:.1f}x")
            print()
    
    def interactive_demo(self):
        """交互式演示"""
        print("=" * 60)
        print("LSM-Tree 交互式演示")
        print("=" * 60)
        
        self.lsm = LSMTree(data_dir="./interactive_demo", max_memtable_size=5)
        
        print("输入命令进行操作:")
        print("  put <key> <value>  - 插入键值对")
        print("  get <key>         - 获取值")
        print("  delete <key>      - 删除键")
        print("  stats             - 显示统计信息")
        print("  quit              - 退出")
        print()
        
        while True:
            try:
                command = input("> ").strip().split()
                
                if not command:
                    continue
                
                if command[0] == "quit":
                    break
                elif command[0] == "put" and len(command) == 3:
                    key, value = command[1], command[2]
                    self.lsm.put(key, value)
                    print(f"插入: {key} -> {value}")
                    
                    # 显示状态
                    stats = self.lsm.get_stats()
                    print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
                    
                elif command[0] == "get" and len(command) == 2:
                    key = command[1]
                    value = self.lsm.get(key)
                    if value is not None:
                        print(f"找到: {key} -> {value}")
                    else:
                        print(f"未找到: {key}")
                        
                elif command[0] == "delete" and len(command) == 2:
                    key = command[1]
                    if self.lsm.delete(key):
                        print(f"删除: {key}")
                    else:
                        print(f"键不存在: {key}")
                        
                elif command[0] == "stats":
                    stats = self.lsm.get_stats()
                    print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
                    print("SSTables:")
                    for level_stat in stats['levels']:
                        if level_stat['sstable_count'] > 0:
                            print(f"  Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")
                
                else:
                    print("无效命令")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"错误: {e}")
        
        print("\n演示结束!")
    
    def run_all_visualizations(self):
        """运行所有可视化演示"""
        self.visualize_memtable_flush()
        self.visualize_compaction()
        self.visualize_read_process()
        self.visualize_space_usage()
        
        print("\n" + "=" * 60)
        print("所有可视化演示完成!")
        print("=" * 60)
        print("""
        通过可视化演示，你应该能够理解：
        
        1. MemTable Flush:
           - 当MemTable达到容量限制时，数据会被flush到Level 0的SSTable
           - 这是一个顺序写入过程，性能很高
        
        2. Compaction:
           - 当Level N的SSTable数量超过阈值时，会触发Compaction
           - Compaction将多个小的SSTable合并成大的SSTable
           - 数据会从Level N移动到Level N+1
        
        3. 读取过程:
           - 首先在MemTable中查找（最快）
           - 然后在各级SSTable中从新到旧查找
           - 找到第一个匹配的键就返回
        
        4. 空间放大:
           - 同一数据可能存在于多个层级
           - 这是LSM-Tree的权衡：用空间换时间
        """)


if __name__ == "__main__":
    visualizer = LSMTreeVisualizer()
    
    print("选择演示模式:")
    print("1. 自动演示所有可视化")
    print("2. 交互式演示")
    
    choice = input("请选择 (1/2): ").strip()
    
    if choice == "1":
        visualizer.run_all_visualizations()
    elif choice == "2":
        visualizer.interactive_demo()
    else:
        print("无效选择，运行自动演示")
        visualizer.run_all_visualizations()
