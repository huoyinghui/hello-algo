"""
存储引擎包演示

这个文件演示了新的存储引擎包的功能：
- 模块化的存储后端
- 自动注册机制
- 存储工厂模式
- 扩展性演示
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from storage import (
    StorageFactory, 
    StorageRegistry,
    get_available_storage_types,
    get_storage_info,
    create_storage
)


def demo_storage_registry():
    """演示存储注册表功能"""
    print("=" * 60)
    print("存储注册表演示")
    print("=" * 60)
    
    # 显示已注册的存储类型
    print("已注册的存储类型:")
    for storage_type in get_available_storage_types():
        print(f"  - {storage_type}")
    
    # 显示存储后端信息
    print("\n存储后端信息:")
    storage_info = get_storage_info()
    for storage_type, backend_class in storage_info.items():
        print(f"  {storage_type}: {backend_class}")
    
    # 检查特定存储类型是否支持
    print("\n检查存储类型支持:")
    test_types = ['pickle', 'json', 'memory', 'excel', 's3', 'unknown']
    for storage_type in test_types:
        is_supported = StorageFactory.is_supported(storage_type)
        print(f"  {storage_type}: {'✓' if is_supported else '✗'}")


def demo_storage_factory():
    """演示存储工厂功能"""
    print("\n" + "=" * 60)
    print("存储工厂演示")
    print("=" * 60)
    
    # 测试不同存储后端的创建
    storage_configs = [
        ('memory', {}),
        ('pickle', {'base_path': '../data/factory_demo_pickle'}),
        ('json', {'base_path': '../data/factory_demo_json'}),
    ]
    
    for storage_type, config in storage_configs:
        print(f"\n--- 创建 {storage_type.upper()} 存储后端 ---")
        
        try:
            # 使用工厂创建存储后端
            storage = StorageFactory.create_storage(storage_type, config)
            print(f"创建成功: {storage}")
            
            # 测试基本操作
            test_data = {'key1': 'value1', 'key2': 'value2'}
            storage.write('test_key', test_data)
            
            # 读取数据
            result = storage.read('test_key')
            print(f"写入和读取结果: {result}")
            
            # 获取统计信息
            stats = storage.get_stats()
            print(f"统计信息: {stats}")
            
            # 清理
            storage.cleanup()
            
        except Exception as e:
            print(f"创建失败: {e}")


def demo_storage_switching():
    """演示存储后端切换"""
    print("\n" + "=" * 60)
    print("存储后端切换演示")
    print("=" * 60)
    
    # 从内存存储开始
    print("1. 创建内存存储")
    memory_storage = create_storage('memory')
    
    # 写入数据
    test_data = {
        'user_1': 'Alice',
        'user_2': 'Bob', 
        'user_3': 'Charlie'
    }
    
    memory_storage.write('users', test_data)
    print(f"写入数据: {test_data}")
    
    # 读取数据
    result = memory_storage.read('users')
    print(f"读取数据: {result}")
    
    # 切换到JSON存储
    print("\n2. 切换到JSON存储")
    json_config = {'base_path': '../data/switching_demo'}
    json_storage = create_storage('json', json_config)
    
    # 迁移数据
    json_storage.write('users', test_data)
    print("数据已迁移到JSON存储")
    
    # 验证迁移
    migrated_data = json_storage.read('users')
    print(f"迁移后数据: {migrated_data}")
    
    # 清理
    memory_storage.cleanup()
    json_storage.cleanup()


def demo_custom_storage_backend():
    """演示如何创建自定义存储后端"""
    print("\n" + "=" * 60)
    print("自定义存储后端演示")
    print("=" * 60)
    
    # 创建一个简单的自定义存储后端
    from storage.core.interface import StorageBackend, StorageConfig
    
    class CustomStorage(StorageBackend):
        """自定义存储后端示例"""
        
        def _setup(self):
            """设置自定义存储"""
            self.data = {}
            print(f"自定义存储后端初始化: {self.config.config}")
        
        def write(self, key, data):
            self.data[key] = data
            return True
        
        def read(self, key):
            return self.data.get(key)
        
        def delete(self, key):
            if key in self.data:
                del self.data[key]
                return True
            return False
        
        def exists(self, key):
            return key in self.data
        
        def list_keys(self):
            return list(self.data.keys())
        
        def get_stats(self):
            return {
                'type': 'custom',
                'total_keys': len(self.data),
                'config': self.config.config
            }
        
        def cleanup(self):
            self.data.clear()
    
    # 手动注册自定义存储后端
    print("注册自定义存储后端...")
    StorageRegistry.register('custom', CustomStorage)
    
    # 使用自定义存储后端
    print("使用自定义存储后端:")
    custom_storage = StorageFactory.create_storage('custom', {'custom_param': 'test'})
    
    # 测试操作
    test_data = {'custom_key': 'custom_value'}
    custom_storage.write('test', test_data)
    
    result = custom_storage.read('test')
    print(f"自定义存储结果: {result}")
    
    stats = custom_storage.get_stats()
    print(f"自定义存储统计: {stats}")
    
    # 清理
    custom_storage.cleanup()
    
    # 注销自定义存储后端
    StorageRegistry.unregister('custom')
    print("已注销自定义存储后端")


def demo_storage_performance():
    """演示存储性能对比"""
    print("\n" + "=" * 60)
    print("存储性能对比演示")
    print("=" * 60)
    
    import time
    
    # 测试数据
    test_data = {f'key_{i}': f'value_{i}' for i in range(100)}
    
    # 测试不同存储后端
    storage_configs = [
        ('memory', {}),
        ('pickle', {'base_path': '../data/perf_demo_pickle'}),
        ('json', {'base_path': '../data/perf_demo_json'}),
    ]
    
    for storage_type, config in storage_configs:
        print(f"\n--- {storage_type.upper()} 存储性能测试 ---")
        
        try:
            storage = create_storage(storage_type, config)
            
            # 写入性能测试
            start_time = time.time()
            for i in range(50):
                key = f'perf_key_{i}'
                data = {f'item_{j}': f'value_{j}' for j in range(10)}
                storage.write(key, data)
            write_time = time.time() - start_time
            
            # 读取性能测试
            start_time = time.time()
            for i in range(50):
                key = f'perf_key_{i}'
                storage.read(key)
            read_time = time.time() - start_time
            
            print(f"写入50个键值对耗时: {write_time:.4f}秒")
            print(f"读取50个键值对耗时: {read_time:.4f}秒")
            print(f"平均写入速度: {50/write_time:.0f} ops/sec")
            print(f"平均读取速度: {50/read_time:.0f} ops/sec")
            
            # 获取统计信息
            stats = storage.get_stats()
            print(f"存储统计: {stats}")
            
            # 清理
            storage.cleanup()
            
        except Exception as e:
            print(f"性能测试失败: {e}")


def demo_storage_context_manager():
    """演示存储上下文管理器"""
    print("\n" + "=" * 60)
    print("存储上下文管理器演示")
    print("=" * 60)
    
    # 使用上下文管理器
    print("使用上下文管理器:")
    with create_storage('memory') as storage:
        # 写入数据
        test_data = {'context_key': 'context_value'}
        storage.write('context_test', test_data)
        
        # 读取数据
        result = storage.read('context_test')
        print(f"上下文管理器结果: {result}")
        
        # 获取统计信息
        stats = storage.get_stats()
        print(f"上下文管理器统计: {stats}")
    
    print("上下文管理器自动清理完成")


if __name__ == "__main__":
    # 运行所有演示
    demo_storage_registry()
    demo_storage_factory()
    demo_storage_switching()
    demo_custom_storage_backend()
    demo_storage_performance()
    demo_storage_context_manager()
    
    print("\n" + "=" * 60)
    print("存储引擎包演示完成！")
    print("=" * 60)
    print("""
    总结：
    1. 存储引擎包提供了模块化的存储后端架构
    2. 支持自动注册和发现存储后端
    3. 使用工厂模式创建存储实例
    4. 支持动态切换存储后端
    5. 易于扩展自定义存储后端
    6. 提供上下文管理器支持
    7. 包含完整的性能测试功能
    """)
