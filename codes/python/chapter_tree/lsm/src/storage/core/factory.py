"""
存储工厂

创建存储后端实例的工厂类。
"""

from typing import Dict, Any, Optional
from .interface import StorageBackend, StorageConfig
from .registry import StorageRegistry


class StorageFactory:
    """存储工厂类"""
    
    @staticmethod
    def create_storage(storage_type: str, config: Dict[str, Any] = None) -> StorageBackend:
        """创建存储后端实例"""
        config = config or {}
        storage_config = StorageConfig(storage_type=storage_type, config=config)
        
        # 获取存储后端类
        backend_class = StorageRegistry.get_backend_class(storage_type)
        
        # 创建实例
        return backend_class(storage_config)
    
    @staticmethod
    def get_available_types() -> list:
        """获取可用的存储类型"""
        return StorageRegistry.list_registered_types()
    
    @staticmethod
    def is_supported(storage_type: str) -> bool:
        """检查存储类型是否支持"""
        return StorageRegistry.is_registered(storage_type)
    
    @staticmethod
    def get_registry_info() -> Dict[str, str]:
        """获取注册表信息"""
        return StorageRegistry.get_registry_info()
    
    @staticmethod
    def create_with_config(storage_config: StorageConfig) -> StorageBackend:
        """使用配置对象创建存储后端"""
        backend_class = StorageRegistry.get_backend_class(storage_config.storage_type)
        return backend_class(storage_config)
