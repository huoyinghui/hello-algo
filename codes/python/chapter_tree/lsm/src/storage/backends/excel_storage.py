"""
Excel存储后端实现

支持Excel文件存储。
"""

import os
import json
from typing import Dict, Any, Optional, List
from datetime import datetime
from ..core.interface import StorageBackend, StorageConfig
from ..core.registry import register_storage


class ExcelFileStorage(StorageBackend):
    """Excel文件存储后端"""
    
    def _setup(self):
        """设置Excel存储"""
        self.base_path = self.config.config.get('base_path', './storage')
        self.excel_file = self.config.config.get('excel_file', 'lsm_data.xlsx')
        self.sheet_name = self.config.config.get('sheet_name', 'SSTables')
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
    
    def cleanup(self):
        """清理资源"""
        pass


# 注册存储后端
register_storage('excel')(ExcelFileStorage)
