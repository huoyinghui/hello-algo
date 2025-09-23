"""
LSM-Tree 使用示例

这个文件展示了如何使用LSM-Tree V2的不同存储后端
"""

from lsm_tree_v2 import LSMTreeV2
from storage_interface import StorageFactory


def example_basic_usage():
    """基本使用示例"""
    print("=== 基本使用示例 ===")
    
    # 创建LSM-Tree实例（使用默认的pickle存储）
    lsm = LSMTreeV2(max_memtable_size=5)
    
    # 插入数据
    lsm.put("user_1", "Alice")
    lsm.put("user_2", "Bob")
    lsm.put("user_3", "Charlie")
    
    # 读取数据
    print(f"用户1: {lsm.get('user_1')}")
    print(f"用户2: {lsm.get('user_2')}")
    print(f"用户3: {lsm.get('user_3')}")
    
    # 显示统计信息
    stats = lsm.get_stats()
    print(f"存储类型: {stats['storage_type']}")
    print(f"MemTable大小: {stats['memtable_size']}/{stats['memtable_max_size']}")


def example_json_storage():
    """JSON存储示例"""
    print("\n=== JSON存储示例 ===")
    
    # 创建使用JSON存储的LSM-Tree
    config = {'base_path': './example_json_data'}
    lsm = LSMTreeV2(storage_type='json', storage_config=config, max_memtable_size=3)
    
    # 插入数据
    products = [
        ("product_1", "iPhone 15"),
        ("product_2", "Samsung Galaxy"),
        ("product_3", "Google Pixel"),
        ("product_4", "OnePlus"),  # 触发flush
    ]
    
    for key, value in products:
        lsm.put(key, value)
        print(f"插入: {key} -> {value}")
    
    # 读取数据
    print("\n读取产品信息:")
    for key, _ in products:
        value = lsm.get(key)
        print(f"  {key}: {value}")
    
    # 显示统计信息
    stats = lsm.get_stats()
    print(f"\nJSON存储统计: {stats['storage_stats']}")


def example_excel_storage():
    """Excel存储示例"""
    print("\n=== Excel存储示例 ===")
    
    try:
        # 创建使用Excel存储的LSM-Tree
        config = {
            'base_path': './example_excel_data',
            'excel_file': 'products.xlsx',
            'sheet_name': 'ProductData'
        }
        lsm = LSMTreeV2(storage_type='excel', storage_config=config, max_memtable_size=3)
        
        # 插入数据
        orders = [
            ("order_1", "Order #1001"),
            ("order_2", "Order #1002"),
            ("order_3", "Order #1003"),
            ("order_4", "Order #1004"),  # 触发flush
        ]
        
        for key, value in orders:
            lsm.put(key, value)
            print(f"插入: {key} -> {value}")
        
        # 读取数据
        print("\n读取订单信息:")
        for key, _ in orders:
            value = lsm.get(key)
            print(f"  {key}: {value}")
        
        # 显示统计信息
        stats = lsm.get_stats()
        print(f"\nExcel存储统计: {stats['storage_stats']}")
        
    except ImportError:
        print("Excel存储需要安装pandas和openpyxl:")
        print("pip install pandas openpyxl")


def example_memory_storage():
    """内存存储示例"""
    print("\n=== 内存存储示例 ===")
    
    # 创建使用内存存储的LSM-Tree
    lsm = LSMTreeV2(storage_type='memory', max_memtable_size=3)
    
    # 插入数据
    cache_data = [
        ("cache_1", "Cached Data 1"),
        ("cache_2", "Cached Data 2"),
        ("cache_3", "Cached Data 3"),
        ("cache_4", "Cached Data 4"),  # 触发flush
    ]
    
    for key, value in cache_data:
        lsm.put(key, value)
        print(f"插入: {key} -> {value}")
    
    # 读取数据
    print("\n读取缓存数据:")
    for key, _ in cache_data:
        value = lsm.get(key)
        print(f"  {key}: {value}")
    
    # 显示统计信息
    stats = lsm.get_stats()
    print(f"\n内存存储统计: {stats['storage_stats']}")


def example_storage_switching():
    """存储切换示例"""
    print("\n=== 存储切换示例 ===")
    
    # 从内存存储开始
    lsm = LSMTreeV2(storage_type='memory', max_memtable_size=3)
    
    # 插入数据
    print("1. 在内存存储中插入数据")
    data = [
        ("item_1", "Item 1"),
        ("item_2", "Item 2"),
        ("item_3", "Item 3"),
        ("item_4", "Item 4"),  # 触发flush
    ]
    
    for key, value in data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    # 切换到JSON存储
    print("\n2. 切换到JSON存储")
    json_config = {'base_path': './switched_example_data'}
    lsm.switch_storage('json', json_config)
    
    # 验证数据迁移
    print("验证数据迁移:")
    for key, _ in data:
        value = lsm.get(key)
        print(f"  读取 {key}: {value}")
    
    # 插入新数据
    print("\n3. 插入新数据")
    new_data = [
        ("item_5", "Item 5"),
        ("item_6", "Item 6"),
    ]
    
    for key, value in new_data:
        lsm.put(key, value)
        print(f"  插入: {key} -> {value}")
    
    # 显示最终状态
    stats = lsm.get_stats()
    print(f"\n最终状态: {stats['storage_type']} 存储")
    print(f"MemTable: {stats['memtable_size']}/{stats['memtable_max_size']}")
    for level_stat in stats['levels']:
        if level_stat['sstable_count'] > 0:
            print(f"Level {level_stat['level']}: {level_stat['sstable_count']} SSTables, {level_stat['total_keys']} keys")


def example_performance_comparison():
    """性能对比示例"""
    print("\n=== 性能对比示例 ===")
    
    import time
    
    # 测试数据
    test_data = [(f"key_{i}", f"value_{i}") for i in range(50)]
    
    # 测试不同存储后端
    storage_configs = [
        ('memory', {}),
        ('pickle', {'base_path': '../data/perf_pickle'}),
        ('json', {'base_path': '../data/perf_json'}),
    ]
    
    for storage_type, config in storage_configs:
        print(f"\n--- {storage_type.upper()} 存储性能测试 ---")
        
        # 创建LSM-Tree
        lsm = LSMTreeV2(storage_type=storage_type, storage_config=config, max_memtable_size=20)
        
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
        
        print(f"写入50个键值对耗时: {write_time:.4f}秒")
        print(f"读取50个键值对耗时: {read_time:.4f}秒")
        print(f"平均写入速度: {50/write_time:.0f} ops/sec")
        print(f"平均读取速度: {50/read_time:.0f} ops/sec")


def example_custom_storage():
    """自定义存储示例"""
    print("\n=== 自定义存储示例 ===")
    
    # 创建自定义存储配置
    custom_configs = {
        'pickle': {
            'base_path': './custom_pickle',
            'description': '自定义Pickle存储路径'
        },
        'json': {
            'base_path': './custom_json',
            'description': '自定义JSON存储路径'
        }
    }
    
    for storage_type, config in custom_configs.items():
        print(f"\n--- 自定义 {storage_type.upper()} 存储 ---")
        print(f"配置: {config}")
        
        lsm = LSMTreeV2(storage_type=storage_type, storage_config=config, max_memtable_size=3)
        
        # 插入测试数据
        test_data = [
            ("custom_1", "Custom Data 1"),
            ("custom_2", "Custom Data 2"),
            ("custom_3", "Custom Data 3"),
        ]
        
        for key, value in test_data:
            lsm.put(key, value)
            print(f"  插入: {key} -> {value}")
        
        # 读取数据
        for key, _ in test_data:
            value = lsm.get(key)
            print(f"  读取 {key}: {value}")
        
        # 显示统计信息
        stats = lsm.get_stats()
        print(f"  存储统计: {stats['storage_stats']}")


if __name__ == "__main__":
    # 运行所有示例
    example_basic_usage()
    example_json_storage()
    example_excel_storage()
    example_memory_storage()
    example_storage_switching()
    example_performance_comparison()
    example_custom_storage()
    
    print("\n=== 所有示例完成 ===")
    print("""
    总结：
    1. LSM-Tree V2支持多种存储后端
    2. 可以动态切换存储类型
    3. 每种存储都有其适用场景
    4. 性能特点各不相同
    5. 可以根据需求选择合适的存储后端
    """)
