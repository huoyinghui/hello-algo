"""
LSM-Tree 核心代码包

这个包包含了LSM-Tree的核心实现：
- LSM-Tree基础实现
- LSM-Tree V2 (支持多种存储后端)
- 存储抽象接口
"""

from .lsm_tree import LSMTree, MemTable, SSTable, BloomFilter
from .lsm_tree_v2 import LSMTreeV2
from .storage_interface import (
    StorageBackend, 
    StorageFactory,
    PickleFileStorage,
    JSONFileStorage,
    ExcelFileStorage,
    S3Storage,
    MemoryStorage
)

__version__ = "2.0.0"
__author__ = "LSM-Tree Implementation"

__all__ = [
    # LSM-Tree基础实现
    "LSMTree",
    "MemTable", 
    "SSTable",
    "BloomFilter",
    
    # LSM-Tree V2
    "LSMTreeV2",
    
    # 存储接口
    "StorageBackend",
    "StorageFactory",
    "PickleFileStorage",
    "JSONFileStorage", 
    "ExcelFileStorage",
    "S3Storage",
    "MemoryStorage"
]
