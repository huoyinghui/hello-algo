"""
LSM-Tree 存储引擎包

这个包提供了完整的存储抽象，支持多种存储后端：
- 文件存储 (Pickle, JSON)
- Excel存储
- 内存存储
- S3云存储
- 可扩展的存储后端架构
"""

# 导入核心接口
from .core import StorageBackend, StorageConfig, StorageRegistry, StorageFactory

# 导入所有存储后端（这会自动注册它们）
from .backends import (
    PickleFileStorage,
    JSONFileStorage,
    ExcelFileStorage,
    MemoryStorage,
    S3Storage
)

__version__ = "2.0.0"
__author__ = "LSM-Tree Storage Engine"

__all__ = [
    # 核心接口
    "StorageBackend",
    "StorageConfig",
    "StorageRegistry", 
    "StorageFactory",
    
    # 存储后端
    "PickleFileStorage",
    "JSONFileStorage",
    "ExcelFileStorage",
    "MemoryStorage",
    "S3Storage"
]


def get_available_storage_types():
    """获取所有可用的存储类型"""
    return StorageFactory.get_available_types()


def create_storage(storage_type: str, config: dict = None):
    """创建存储后端实例"""
    return StorageFactory.create_storage(storage_type, config)


def get_storage_info():
    """获取存储后端信息"""
    return StorageFactory.get_registry_info()
