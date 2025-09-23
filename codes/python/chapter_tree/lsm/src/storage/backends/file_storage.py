"""
文件存储后端实现

支持Pickle和JSON文件存储。
"""

import os
import json
import pickle
from typing import Dict, Any, Optional, List
from ..core.interface import StorageBackend, StorageConfig
from ..core.registry import register_storage


class PickleFileStorage(StorageBackend):
    """Pickle文件存储后端"""
    
    def _setup(self):
        """设置Pickle存储"""
        self.base_path = self.config.config.get('base_path', './storage')
        os.makedirs(self.base_path, exist_ok=True)
    
    def write(self, key: str, data: Dict[str, Any]) -> bool:
        """写入Pickle文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, f"{key}.pkl")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'wb') as f:
                    pickle.dump(data, f)
                return True
        except Exception as e:
            print(f"Pickle写入失败: {e}")
            return False
    
    def read(self, key: str) -> Optional[Dict[str, Any]]:
        """读取Pickle文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, f"{key}.pkl")
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as f:
                        return pickle.load(f)
                return None
        except Exception as e:
            print(f"Pickle读取失败: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """删除Pickle文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, f"{key}.pkl")
                if os.path.exists(file_path):
                    os.remove(file_path)
                    return True
                return False
        except Exception as e:
            print(f"Pickle删除失败: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """检查Pickle文件是否存在"""
        file_path = os.path.join(self.base_path, f"{key}.pkl")
        return os.path.exists(file_path)
    
    def list_keys(self) -> List[str]:
        """列出所有Pickle文件键"""
        try:
            keys = []
            for filename in os.listdir(self.base_path):
                if filename.endswith('.pkl'):
                    keys.append(filename[:-4])  # 移除.pkl后缀
            return keys
        except Exception:
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """获取Pickle存储统计信息"""
        try:
            total_files = len([f for f in os.listdir(self.base_path) if f.endswith('.pkl')])
            total_size = sum(
                os.path.getsize(os.path.join(self.base_path, f))
                for f in os.listdir(self.base_path)
                if f.endswith('.pkl')
            )
            return {
                'type': 'pickle',
                'base_path': self.base_path,
                'total_files': total_files,
                'total_size_bytes': total_size
            }
        except Exception:
            return {'type': 'pickle', 'base_path': self.base_path, 'total_files': 0, 'total_size_bytes': 0}
    
    def cleanup(self):
        """清理资源"""
        pass


class JSONFileStorage(StorageBackend):
    """JSON文件存储后端"""
    
    def _setup(self):
        """设置JSON存储"""
        self.base_path = self.config.config.get('base_path', './storage')
        os.makedirs(self.base_path, exist_ok=True)
    
    def write(self, key: str, data: Dict[str, Any]) -> bool:
        """写入JSON文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, f"{key}.json")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                return True
        except Exception as e:
            print(f"JSON写入失败: {e}")
            return False
    
    def read(self, key: str) -> Optional[Dict[str, Any]]:
        """读取JSON文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, f"{key}.json")
                if os.path.exists(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                return None
        except Exception as e:
            print(f"JSON读取失败: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """删除JSON文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, f"{key}.json")
                if os.path.exists(file_path):
                    os.remove(file_path)
                    return True
                return False
        except Exception as e:
            print(f"JSON删除失败: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """检查JSON文件是否存在"""
        file_path = os.path.join(self.base_path, f"{key}.json")
        return os.path.exists(file_path)
    
    def list_keys(self) -> List[str]:
        """列出所有JSON文件键"""
        try:
            keys = []
            for filename in os.listdir(self.base_path):
                if filename.endswith('.json'):
                    keys.append(filename[:-5])  # 移除.json后缀
            return keys
        except Exception:
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """获取JSON存储统计信息"""
        try:
            total_files = len([f for f in os.listdir(self.base_path) if f.endswith('.json')])
            total_size = sum(
                os.path.getsize(os.path.join(self.base_path, f))
                for f in os.listdir(self.base_path)
                if f.endswith('.json')
            )
            return {
                'type': 'json',
                'base_path': self.base_path,
                'total_files': total_files,
                'total_size_bytes': total_size
            }
        except Exception:
            return {'type': 'json', 'base_path': self.base_path, 'total_files': 0, 'total_size_bytes': 0}
    
    def cleanup(self):
        """清理资源"""
        pass


# 注册存储后端
register_storage('pickle')(PickleFileStorage)
register_storage('json')(JSONFileStorage)
