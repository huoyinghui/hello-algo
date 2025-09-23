"""
存储引擎核心模块

这个模块定义了存储引擎的核心接口和抽象类。
"""

from .interface import StorageBackend, StorageConfig
from .registry import StorageRegistry
from .factory import StorageFactory

__all__ = [
    "StorageBackend",
    "StorageConfig", 
    "StorageRegistry",
    "StorageFactory"
]
