"""
存储引擎核心接口

定义了存储引擎的核心接口和抽象类。
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
import threading
from dataclasses import dataclass


@dataclass
class StorageConfig:
    """存储配置类"""
    storage_type: str
    config: Dict[str, Any]
    
    def __post_init__(self):
        """验证配置"""
        if not self.storage_type:
            raise ValueError("storage_type不能为空")
        if not isinstance(self.config, dict):
            raise ValueError("config必须是字典类型")


class StorageBackend(ABC):
    """存储后端抽象基类"""
    
    def __init__(self, config: StorageConfig):
        self.config = config
        self.lock = threading.RLock()
        self._initialized = False
        self._initialize()
    
    def _initialize(self):
        """初始化存储后端"""
        if not self._initialized:
            self._setup()
            self._initialized = True
    
    @abstractmethod
    def _setup(self):
        """设置存储后端"""
        pass
    
    @abstractmethod
    def write(self, key: str, data: Dict[str, Any]) -> bool:
        """写入数据"""
        pass
    
    @abstractmethod
    def read(self, key: str) -> Optional[Dict[str, Any]]:
        """读取数据"""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """删除数据"""
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        """检查数据是否存在"""
        pass
    
    @abstractmethod
    def list_keys(self) -> List[str]:
        """列出所有键"""
        pass
    
    @abstractmethod
    def get_stats(self) -> Dict[str, Any]:
        """获取存储统计信息"""
        pass
    
    @abstractmethod
    def cleanup(self):
        """清理资源"""
        pass
    
    def __enter__(self):
        """上下文管理器入口"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.cleanup()
    
    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.config.storage_type})"
