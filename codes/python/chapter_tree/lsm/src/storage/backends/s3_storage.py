"""
S3存储后端实现

支持AWS S3云存储。
"""

import json
from typing import Dict, Any, Optional, List
from ..core.interface import StorageBackend, StorageConfig
from ..core.registry import register_storage


class S3Storage(StorageBackend):
    """S3网络存储后端"""
    
    def _setup(self):
        """设置S3存储"""
        self.bucket_name = self.config.config.get('bucket_name', 'lsm-tree-bucket')
        self.region = self.config.config.get('region', 'us-east-1')
        self.prefix = self.config.config.get('prefix', 'sstables/')
        
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
    
    def cleanup(self):
        """清理资源"""
        pass


# 注册存储后端
register_storage('s3')(S3Storage)
