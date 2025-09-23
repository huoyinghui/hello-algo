"""
LSM-Tree 存储抽象接口

这个模块定义了LSM-Tree的存储抽象接口，支持多种存储后端：
- 本地文件存储 (pickle, json)
- Excel文件存储
- 网络存储 (S3, HTTP)
- 内存存储
- 数据库存储
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List, Tuple
import os
import json
import pickle
import threading
from datetime import datetime


class StorageBackend(ABC):
    """存储后端抽象基类"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.lock = threading.RLock()
    
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


class PickleFileStorage(StorageBackend):
    """Pickle文件存储后端"""
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.base_path = self.config.get('base_path', './storage')
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


class JSONFileStorage(StorageBackend):
    """JSON文件存储后端"""
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.base_path = self.config.get('base_path', './storage')
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


class ExcelFileStorage(StorageBackend):
    """Excel文件存储后端"""
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.base_path = self.config.get('base_path', './storage')
        self.excel_file = self.config.get('excel_file', 'lsm_data.xlsx')
        self.sheet_name = self.config.get('sheet_name', 'SSTables')
        os.makedirs(self.base_path, exist_ok=True)
        
        # 尝试导入pandas和openpyxl
        try:
            import pandas as pd
            self.pd = pd
        except ImportError:
            raise ImportError("需要安装pandas: pip install pandas openpyxl")
    
    def write(self, key: str, data: Dict[str, Any]) -> bool:
        """写入Excel文件"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, self.excel_file)
                
                # 准备数据
                rows = []
                for k, v in data.items():
                    rows.append({
                        'sstable_key': key,
                        'data_key': k,
                        'data_value': v,
                        'timestamp': datetime.now().isoformat()
                    })
                
                # 读取现有数据
                if os.path.exists(file_path):
                    try:
                        df_existing = self.pd.read_excel(file_path, sheet_name=self.sheet_name)
                    except:
                        df_existing = self.pd.DataFrame()
                else:
                    df_existing = self.pd.DataFrame()
                
                # 合并数据
                df_new = self.pd.DataFrame(rows)
                df_combined = self.pd.concat([df_existing, df_new], ignore_index=True)
                
                # 写入Excel
                with self.pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                    df_combined.to_excel(writer, sheet_name=self.sheet_name, index=False)
                
                return True
        except Exception as e:
            print(f"Excel写入失败: {e}")
            return False
    
    def read(self, key: str) -> Optional[Dict[str, Any]]:
        """从Excel文件读取数据"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, self.excel_file)
                if not os.path.exists(file_path):
                    return None
                
                df = self.pd.read_excel(file_path, sheet_name=self.sheet_name)
                sstable_data = df[df['sstable_key'] == key]
                
                if sstable_data.empty:
                    return None
                
                # 转换为字典
                result = {}
                for _, row in sstable_data.iterrows():
                    result[row['data_key']] = row['data_value']
                
                return result
        except Exception as e:
            print(f"Excel读取失败: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """从Excel文件删除数据"""
        try:
            with self.lock:
                file_path = os.path.join(self.base_path, self.excel_file)
                if not os.path.exists(file_path):
                    return False
                
                df = self.pd.read_excel(file_path, sheet_name=self.sheet_name)
                df_filtered = df[df['sstable_key'] != key]
                
                with self.pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                    df_filtered.to_excel(writer, sheet_name=self.sheet_name, index=False)
                
                return True
        except Exception as e:
            print(f"Excel删除失败: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """检查Excel文件中是否存在数据"""
        try:
            file_path = os.path.join(self.base_path, self.excel_file)
            if not os.path.exists(file_path):
                return False
            
            df = self.pd.read_excel(file_path, sheet_name=self.sheet_name)
            return not df[df['sstable_key'] == key].empty
        except Exception:
            return False
    
    def list_keys(self) -> List[str]:
        """列出Excel文件中的所有键"""
        try:
            file_path = os.path.join(self.base_path, self.excel_file)
            if not os.path.exists(file_path):
                return []
            
            df = self.pd.read_excel(file_path, sheet_name=self.sheet_name)
            return df['sstable_key'].unique().tolist()
        except Exception:
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """获取Excel存储统计信息"""
        try:
            file_path = os.path.join(self.base_path, self.excel_file)
            if not os.path.exists(file_path):
                return {
                    'type': 'excel',
                    'excel_file': self.excel_file,
                    'total_records': 0,
                    'file_size_bytes': 0
                }
            
            df = self.pd.read_excel(file_path, sheet_name=self.sheet_name)
            file_size = os.path.getsize(file_path)
            
            return {
                'type': 'excel',
                'excel_file': self.excel_file,
                'total_records': len(df),
                'file_size_bytes': file_size
            }
        except Exception:
            return {'type': 'excel', 'excel_file': self.excel_file, 'total_records': 0, 'file_size_bytes': 0}


class S3Storage(StorageBackend):
    """S3网络存储后端"""
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.bucket_name = self.config.get('bucket_name', 'lsm-tree-bucket')
        self.region = self.config.get('region', 'us-east-1')
        self.prefix = self.config.get('prefix', 'sstables/')
        
        # 尝试导入boto3
        try:
            import boto3
            self.s3_client = boto3.client('s3', region_name=self.region)
        except ImportError:
            raise ImportError("需要安装boto3: pip install boto3")
    
    def write(self, key: str, data: Dict[str, Any]) -> bool:
        """写入S3"""
        try:
            with self.lock:
                s3_key = f"{self.prefix}{key}.json"
                json_data = json.dumps(data, ensure_ascii=False)
                
                self.s3_client.put_object(
                    Bucket=self.bucket_name,
                    Key=s3_key,
                    Body=json_data.encode('utf-8'),
                    ContentType='application/json'
                )
                return True
        except Exception as e:
            print(f"S3写入失败: {e}")
            return False
    
    def read(self, key: str) -> Optional[Dict[str, Any]]:
        """从S3读取"""
        try:
            with self.lock:
                s3_key = f"{self.prefix}{key}.json"
                response = self.s3_client.get_object(Bucket=self.bucket_name, Key=s3_key)
                json_data = response['Body'].read().decode('utf-8')
                return json.loads(json_data)
        except Exception as e:
            print(f"S3读取失败: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """从S3删除"""
        try:
            with self.lock:
                s3_key = f"{self.prefix}{key}.json"
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=s3_key)
                return True
        except Exception as e:
            print(f"S3删除失败: {e}")
            return False
    
    def exists(self, key: str) -> bool:
        """检查S3中是否存在"""
        try:
            s3_key = f"{self.prefix}{key}.json"
            self.s3_client.head_object(Bucket=self.bucket_name, Key=s3_key)
            return True
        except:
            return False
    
    def list_keys(self) -> List[str]:
        """列出S3中的所有键"""
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=self.prefix
            )
            keys = []
            for obj in response.get('Contents', []):
                key = obj['Key']
                if key.endswith('.json'):
                    keys.append(key[len(self.prefix):-5])  # 移除前缀和.json后缀
            return keys
        except Exception:
            return []
    
    def get_stats(self) -> Dict[str, Any]:
        """获取S3存储统计信息"""
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=self.prefix
            )
            total_objects = len(response.get('Contents', []))
            total_size = sum(obj['Size'] for obj in response.get('Contents', []))
            
            return {
                'type': 's3',
                'bucket_name': self.bucket_name,
                'region': self.region,
                'total_objects': total_objects,
                'total_size_bytes': total_size
            }
        except Exception:
            return {
                'type': 's3',
                'bucket_name': self.bucket_name,
                'region': self.region,
                'total_objects': 0,
                'total_size_bytes': 0
            }


class MemoryStorage(StorageBackend):
    """内存存储后端（用于测试）"""
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
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


class StorageFactory:
    """存储工厂类"""
    
    @staticmethod
    def create_storage(storage_type: str, config: Dict[str, Any] = None) -> StorageBackend:
        """创建存储后端实例"""
        config = config or {}
        
        if storage_type.lower() == 'pickle':
            return PickleFileStorage(config)
        elif storage_type.lower() == 'json':
            return JSONFileStorage(config)
        elif storage_type.lower() == 'excel':
            return ExcelFileStorage(config)
        elif storage_type.lower() == 's3':
            return S3Storage(config)
        elif storage_type.lower() == 'memory':
            return MemoryStorage(config)
        else:
            raise ValueError(f"不支持的存储类型: {storage_type}")
    
    @staticmethod
    def get_available_types() -> List[str]:
        """获取可用的存储类型"""
        return ['pickle', 'json', 'excel', 's3', 'memory']


# 测试代码
if __name__ == "__main__":
    # 测试不同存储后端
    test_data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    
    print("=== 存储后端测试 ===")
    
    # 测试Pickle存储
    print("\n1. 测试Pickle存储")
    pickle_storage = StorageFactory.create_storage('pickle', {'base_path': './test_pickle'})
    pickle_storage.write('test_key', test_data)
    result = pickle_storage.read('test_key')
    print(f"写入和读取结果: {result}")
    print(f"统计信息: {pickle_storage.get_stats()}")
    
    # 测试JSON存储
    print("\n2. 测试JSON存储")
    json_storage = StorageFactory.create_storage('json', {'base_path': './test_json'})
    json_storage.write('test_key', test_data)
    result = json_storage.read('test_key')
    print(f"写入和读取结果: {result}")
    print(f"统计信息: {json_storage.get_stats()}")
    
    # 测试内存存储
    print("\n3. 测试内存存储")
    memory_storage = StorageFactory.create_storage('memory')
    memory_storage.write('test_key', test_data)
    result = memory_storage.read('test_key')
    print(f"写入和读取结果: {result}")
    print(f"统计信息: {memory_storage.get_stats()}")
    
    print("\n=== 测试完成 ===")
