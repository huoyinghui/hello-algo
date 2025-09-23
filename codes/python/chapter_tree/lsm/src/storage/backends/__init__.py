"""
存储后端实现

这个模块包含了各种存储后端的具体实现。
"""

from .file_storage import PickleFileStorage, JSONFileStorage
from .excel_storage import ExcelFileStorage
from .memory_storage import MemoryStorage
from .s3_storage import S3Storage

# 自动注册所有存储后端
from .auto_register import register_all_backends

# 注册所有存储后端
register_all_backends()

__all__ = [
    "PickleFileStorage",
    "JSONFileStorage", 
    "ExcelFileStorage",
    "MemoryStorage",
    "S3Storage",
    "register_all_backends"
]
