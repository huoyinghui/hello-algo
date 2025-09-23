"""
内存存储后端实现

用于测试和临时存储的内存存储后端。
"""

from typing import Dict, Any, Optional, List
from ..core.interface import StorageBackend, StorageConfig
from ..core.registry import register_storage


class MemoryStorage(StorageBackend):
    """内存存储后端（用于测试）"""
    
    def _setup(self):
        """设置内存存储"""
        self.data = {}
    
    def write(self, key: str, data: Dict[str, Any]) -> bool:
        """写入内存"""
        with self.lock:
            self.data[key] = data.copy()
            return True
    
    def read(self, key: str) -> Optional[Dict[str, Any]]:
        """从内存读取"""
        with self.lock:
            return self.data.get(key)
    
    def delete(self, key: str) -> bool:
        """从内存删除"""
        with self.lock:
            if key in self.data:
                del self.data[key]
                return True
            return False
    
    def exists(self, key: str) -> bool:
        """检查内存中是否存在"""
        return key in self.data
    
    def list_keys(self) -> List[str]:
        """列出内存中的所有键"""
        with self.lock:
            return list(self.data.keys())
    
    def get_stats(self) -> Dict[str, Any]:
        """获取内存存储统计信息"""
        with self.lock:
            return {
                'type': 'memory',
                'total_keys': len(self.data),
                'memory_usage_bytes': sum(len(str(v)) for v in self.data.values())
            }
    
    def cleanup(self):
        """清理资源"""
        with self.lock:
            self.data.clear()


# 注册存储后端
register_storage('memory')(MemoryStorage)
