"""
存储后端注册表

管理存储后端的注册和发现。
"""

from typing import Dict, Type, List
from .interface import StorageBackend


class StorageRegistry:
    """存储后端注册表"""
    
    _registry: Dict[str, Type[StorageBackend]] = {}
    
    @classmethod
    def register(cls, storage_type: str, backend_class: Type[StorageBackend]):
        """注册存储后端"""
        if not issubclass(backend_class, StorageBackend):
            raise ValueError(f"存储后端必须继承自StorageBackend: {backend_class}")
        
        cls._registry[storage_type.lower()] = backend_class
        print(f"注册存储后端: {storage_type} -> {backend_class.__name__}")
    
    @classmethod
    def unregister(cls, storage_type: str):
        """注销存储后端"""
        storage_type = storage_type.lower()
        if storage_type in cls._registry:
            del cls._registry[storage_type]
            print(f"注销存储后端: {storage_type}")
    
    @classmethod
    def get_backend_class(cls, storage_type: str) -> Type[StorageBackend]:
        """获取存储后端类"""
        storage_type = storage_type.lower()
        if storage_type not in cls._registry:
            raise ValueError(f"未注册的存储类型: {storage_type}")
        return cls._registry[storage_type]
    
    @classmethod
    def list_registered_types(cls) -> List[str]:
        """列出所有已注册的存储类型"""
        return list(cls._registry.keys())
    
    @classmethod
    def is_registered(cls, storage_type: str) -> bool:
        """检查存储类型是否已注册"""
        return storage_type.lower() in cls._registry
    
    @classmethod
    def clear_registry(cls):
        """清空注册表"""
        cls._registry.clear()
        print("清空存储后端注册表")
    
    @classmethod
    def get_registry_info(cls) -> Dict[str, str]:
        """获取注册表信息"""
        return {
            storage_type: backend_class.__name__ 
            for storage_type, backend_class in cls._registry.items()
        }


# 装饰器用于注册存储后端
def register_storage(storage_type: str):
    """存储后端注册装饰器"""
    def decorator(backend_class: Type[StorageBackend]):
        StorageRegistry.register(storage_type, backend_class)
        return backend_class
    return decorator
