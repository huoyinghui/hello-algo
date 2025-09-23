"""
自动注册存储后端

这个模块负责自动注册所有可用的存储后端。
"""

from .file_storage import PickleFileStorage, JSONFileStorage
from .memory_storage import MemoryStorage
from .excel_storage import ExcelFileStorage
from .s3_storage import S3Storage


def register_all_backends():
    """注册所有存储后端"""
    # 导入所有存储后端类会自动触发注册
    # 因为每个存储后端文件都使用了@register_storage装饰器
    
    print("已注册的存储后端:")
    from ..core.registry import StorageRegistry
    for storage_type, backend_class in StorageRegistry.get_registry_info().items():
        print(f"  - {storage_type}: {backend_class}")


def get_available_backends():
    """获取所有可用的存储后端"""
    from ..core.registry import StorageRegistry
    return StorageRegistry.list_registered_types()


def get_backend_info():
    """获取存储后端信息"""
    from ..core.registry import StorageRegistry
    return StorageRegistry.get_registry_info()
