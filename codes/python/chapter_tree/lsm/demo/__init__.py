"""
LSM-Tree 演示和学习资源包

这个包包含了LSM-Tree的演示和学习资源：
- 学习指南
- 可视化工具
- 存储后端演示
- 使用示例
"""

__version__ = "2.0.0"
__author__ = "LSM-Tree Implementation"

# 演示模块说明
DEMO_MODULES = {
    "lsm_tree_guide": "详细学习指南 - 核心概念解释和各种特性演示",
    "lsm_tree_visualizer": "可视化工具 - 直观理解LSM-Tree工作原理",
    "storage_demo": "存储后端演示 - 多种存储后端使用示例和性能对比",
    "usage_examples": "使用示例 - 基本使用和不同存储后端示例"
}

def list_demos():
    """列出所有可用的演示模块"""
    print("可用的演示模块:")
    for module, description in DEMO_MODULES.items():
        print(f"  {module}: {description}")

if __name__ == "__main__":
    list_demos()
