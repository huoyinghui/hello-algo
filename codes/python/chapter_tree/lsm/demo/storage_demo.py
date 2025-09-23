"""
LSM-Tree 存储后端演示

这个文件演示了如何使用不同的存储后端：
- Pickle文件存储
- JSON文件存储
- Excel文件存储
- S3网络存储
- 内存存储
"""

import time
import os
from lsm_tree_v2 import LSMTreeV2
from storage_interface import StorageFactory


def demo_pickle_storage():
    """演示Pickle存储"""
    print("=" * 60)
    print("Pickle 存储后端演示")
    print("=" * 60)
    
    config = {
        'base_path': '../data/demo_pickle_storage'
    }
    
    lsm = LSMTreeV2(storage_type='pickle', storage_config=config, max_memtable_size=5)
    
    print("插入测试数据:")
    test_data = [
        ("user_1", "Alice"),
        ("user_2", "Bob"),
        ("user_3", "Charlie"),
        ("user_4", "David"),
        ("user_5", "Eve"),
        ("user_6", "Frank"),  # 触发flush
    ]
    
    for key, value in test_data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    print("\n读取测试:")
    for key, _ in test_data:
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    stats = lsm.get_stats()
    print(f"\nPickle存储统计: {stats}")
    
    # 清理
    import shutil
    if os.path.exists('./demo_pickle_storage'):
        shutil.rmtree('./demo_pickle_storage')


def demo_json_storage():
    """演示JSON存储"""
    print("\n" + "=" * 60)
    print("JSON 存储后端演示")
    print("=" * 60)
    
    config = {
        'base_path': '../data/demo_json_storage'
    }
    
    lsm = LSMTreeV2(storage_type='json', storage_config=config, max_memtable_size=5)
    
    print("插入测试数据:")
    test_data = [
        ("product_1", "iPhone 15"),
        ("product_2", "Samsung Galaxy"),
        ("product_3", "Google Pixel"),
        ("product_4", "OnePlus"),
        ("product_5", "Xiaomi"),
        ("product_6", "Huawei"),  # 触发flush
    ]
    
    for key, value in test_data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    print("\n读取测试:")
    for key, _ in test_data:
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    stats = lsm.get_stats()
    print(f"\nJSON存储统计: {stats}")
    
    # 清理
    import shutil
    if os.path.exists('./demo_json_storage'):
        shutil.rmtree('./demo_json_storage')


def demo_excel_storage():
    """演示Excel存储"""
    print("\n" + "=" * 60)
    print("Excel 存储后端演示")
    print("=" * 60)
    
    try:
        config = {
            'base_path': '../data/demo_excel_storage',
            'excel_file': 'lsm_data.xlsx',
            'sheet_name': 'SSTables'
        }
        
        lsm = LSMTreeV2(storage_type='excel', storage_config=config, max_memtable_size=5)
        
        print("插入测试数据:")
        test_data = [
            ("order_1", "Order #1001"),
            ("order_2", "Order #1002"),
            ("order_3", "Order #1003"),
            ("order_4", "Order #1004"),
            ("order_5", "Order #1005"),
            ("order_6", "Order #1006"),  # 触发flush
        ]
        
        for key, value in test_data:
            lsm.put(key, value)
            print(f"  插入: {key} -> {value}")
        
        print("\n读取测试:")
        for key, _ in test_data:
            value = lsm.get(key)
            print(f"  读取 {key}: {value}")
        
        stats = lsm.get_stats()
        print(f"\nExcel存储统计: {stats}")
        
        # 清理
        import shutil
        if os.path.exists('./demo_excel_storage'):
            shutil.rmtree('./demo_excel_storage')
            
    except ImportError:
        print("Excel存储需要安装pandas和openpyxl:")
        print("pip install pandas openpyxl")


def demo_memory_storage():
    """演示内存存储"""
    print("\n" + "=" * 60)
    print("内存 存储后端演示")
    print("=" * 60)
    
    lsm = LSMTreeV2(storage_type='memory', max_memtable_size=5)
    
    print("插入测试数据:")
    test_data = [
        ("cache_1", "Cached Data 1"),
        ("cache_2", "Cached Data 2"),
        ("cache_3", "Cached Data 3"),
        ("cache_4", "Cached Data 4"),
        ("cache_5", "Cached Data 5"),
        ("cache_6", "Cached Data 6"),  # 触发flush
    ]
    
    for key, value in test_data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    print("\n读取测试:")
    for key, _ in test_data:
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    stats = lsm.get_stats()
    print(f"\n内存存储统计: {stats}")


def demo_storage_switching():
    """演示存储后端切换"""
    print("\n" + "=" * 60)
    print("存储后端切换演示")
    print("=" * 60)
    
    # 从内存存储开始
    print("1. 从内存存储开始")
    lsm = LSMTreeV2(storage_type='memory', max_memtable_size=3)
    
    # 插入数据
    print("插入初始数据:")
    initial_data = [
        ("data_1", "Initial Data 1"),
        ("data_2", "Initial Data 2"),
        ("data_3", "Initial Data 3"),
        ("data_4", "Initial Data 4"),  # 触发flush
    ]
    
    for key, value in initial_data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    # 显示内存存储状态
    stats = lsm.get_stats()
    print(f"内存存储状态: {stats}")
    
    # 切换到JSON存储
    print("\n2. 切换到JSON存储")
    json_config = {'base_path': './switched_storage'}
    lsm.switch_storage('json', json_config)
    
    # 验证数据迁移
    print("验证数据迁移:")
    for key, _ in initial_data:
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    # 插入新数据
    print("\n插入新数据:")
    new_data = [
        ("data_5", "New Data 5"),
        ("data_6", "New Data 6"),
    ]
    
    for key, value in new_data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    # 显示JSON存储状态
    stats = lsm.get_stats()
    print(f"JSON存储状态: {stats}")
    
    # 切换到Pickle存储
    print("\n3. 切换到Pickle存储")
    pickle_config = {'base_path': './switched_pickle_storage'}
    lsm.switch_storage('pickle', pickle_config)
    
    # 验证所有数据
    print("验证所有数据:")
    all_data = initial_data + new_data
    for key, _ in all_data:
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    # 显示Pickle存储状态
    stats = lsm.get_stats()
    print(f"Pickle存储状态: {stats}")
    
    # 清理
    import shutil
    for path in ['./switched_storage', './switched_pickle_storage']:
        if os.path.exists(path):
            shutil.rmtree(path)


def demo_performance_comparison():
    """演示不同存储后端的性能对比"""
    print("\n" + "=" * 60)
    print("存储后端性能对比")
    print("=" * 60)
    
    storage_configs = [
        ('memory', {}),
        ('pickle', {'base_path': '../data/perf_pickle'}),
        ('json', {'base_path': '../data/perf_json'}),
    ]
    
    test_data = [(f"key_{i}", f"value_{i}") for i in range(100)]
    
    for storage_type, config in storage_configs:
        print(f"\n--- {storage_type.upper()} 存储性能测试 ---")
        
        # 创建LSM-Tree
        lsm = LSMTreeV2(storage_type=storage_type, storage_config=config, max_memtable_size=50)
        
        # 写入性能测试
        start_time = time.time()
        for key, value in test_data:
            lsm.put(key, value)
        write_time = time.time() - start_time
        
        # 读取性能测试
        start_time = time.time()
        for key, _ in test_data:
            lsm.get(key)
        read_time = time.time() - start_time
        
        print(f"写入100个键值对耗时: {write_time:.4f}秒")
        print(f"读取100个键值对耗时: {read_time:.4f}秒")
        print(f"平均写入速度: {100/write_time:.0f} ops/sec")
        print(f"平均读取速度: {100/read_time:.0f} ops/sec")
        
        # 清理
        if storage_type != 'memory':
            import shutil
            if os.path.exists(config['base_path']):
                shutil.rmtree(config['base_path'])


def interactive_storage_demo():
    """交互式存储演示"""
    print("\n" + "=" * 60)
    print("交互式存储演示")
    print("=" * 60)
    
    print("可用的存储类型:")
    available_types = StorageFactory.get_available_types()
    for i, storage_type in enumerate(available_types, 1):
        print(f"  {i}. {storage_type}")
    
    try:
        choice = int(input("请选择存储类型 (1-{}): ".format(len(available_types))))
        if 1 <= choice <= len(available_types):
            selected_type = available_types[choice - 1]
        else:
            selected_type = 'memory'
    except:
        selected_type = 'memory'
    
    # 创建LSM-Tree
    config = {'base_path': f'./interactive_{selected_type}'}
    lsm = LSMTreeV2(storage_type=selected_type, storage_config=config, max_memtable_size=5)
    
    print(f"\n使用 {selected_type} 存储后端")
    print("输入命令进行操作:")
    print("  put <key> <value>  - 插入键值对")
    print("  get <key>         - 获取值")
    print("  delete <key>      - 删除键")
    print("  stats             - 显示统计信息")
    print("  switch <type>     - 切换存储类型")
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
                lsm.put(key, value)
                print(f"插入: {key} -> {value}")
                
            elif command[0] == "get" and len(command) == 2:
                key = command[1]
                value = lsm.get(key)
                if value is not None:
                    print(f"找到: {key} -> {value}")
                else:
                    print(f"未找到: {key}")
                    
            elif command[0] == "delete" and len(command) == 2:
                key = command[1]
                if lsm.delete(key):
                    print(f"删除: {key}")
                else:
                    print(f"键不存在: {key}")
                    
            elif command[0] == "stats":
                stats = lsm.get_stats()
                print(f"存储类型: {stats['storage_type']}")
                print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
                print("SSTables:")
                for level_stat in stats['levels']:
                    if level_stat['sstable_count'] > 0:
                        print(f"  Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")
                print(f"存储统计: {stats['storage_stats']}")
                
            elif command[0] == "switch" and len(command) == 2:
                new_type = command[1]
                if new_type in available_types:
                    lsm.switch_storage(new_type, {'base_path': f'./interactive_{new_type}'})
                    print(f"已切换到 {new_type} 存储")
                else:
                    print(f"不支持的存储类型: {new_type}")
            
            else:
                print("无效命令")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"错误: {e}")
    
    # 清理
    import shutil
    for storage_type in available_types:
        path = f'./interactive_{storage_type}'
        if os.path.exists(path):
            shutil.rmtree(path)
    
    print("\n演示结束!")


if __name__ == "__main__":
    # 运行所有演示
    demo_pickle_storage()
    demo_json_storage()
    demo_excel_storage()
    demo_memory_storage()
    demo_storage_switching()
    demo_performance_comparison()
    
    # 交互式演示
    try:
        interactive_storage_demo()
    except KeyboardInterrupt:
        print("\n演示结束!")
