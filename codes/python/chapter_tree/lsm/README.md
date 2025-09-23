# LSM-Tree 实现和学习资源

这个目录包含了完整的LSM-Tree (Log-Structured Merge-Tree) 实现和学习资源，采用清晰的目录结构组织。

## 📁 目录结构

```
lsm/
├── src/                         # 核心代码
│   ├── lsm_tree.py             # LSM-Tree基础实现
│   ├── lsm_tree_v2.py          # LSM-Tree V2 (支持多种存储后端)
│   ├── lsm_tree_v3.py          # LSM-Tree V3 (使用新的存储引擎包)
│   └── storage/                # 存储引擎包
│       ├── core/               # 核心接口
│       │   ├── interface.py   # 存储接口定义
│       │   ├── registry.py    # 存储注册表
│       │   └── factory.py      # 存储工厂
│       ├── backends/           # 存储后端实现
│       │   ├── file_storage.py    # 文件存储 (Pickle, JSON)
│       │   ├── memory_storage.py  # 内存存储
│       │   ├── excel_storage.py   # Excel存储
│       │   ├── s3_storage.py      # S3云存储
│       │   └── auto_register.py   # 自动注册
│       └── __init__.py         # 存储包入口
├── demo/                        # 演示和学习资源
│   ├── lsm_tree_guide.py       # 详细学习指南
│   ├── lsm_tree_visualizer.py  # 可视化工具
│   ├── storage_demo.py         # 存储后端演示
│   ├── storage_engine_demo.py  # 存储引擎包演示
│   └── usage_examples.py       # 使用示例
├── data/                        # 存储数据文件
│   ├── *_demo/                 # 各种演示生成的数据
│   ├── *_data/                 # 测试数据
│   └── *_visual/               # 可视化数据
├── README.md                   # 项目说明
└── lsm_tree_summary.md         # 学习总结文档
```

## 🚀 快速开始

### 1. 运行基本测试
```bash
cd src
python lsm_tree.py
```

### 2. 测试存储抽象
```bash
cd src
python lsm_tree_v2.py
python lsm_tree_v3.py
```

### 3. 学习核心概念
```bash
cd demo
python lsm_tree_guide.py
```

### 4. 可视化演示
```bash
cd demo
python lsm_tree_visualizer.py
```

### 5. 存储后端演示
```bash
cd demo
python storage_demo.py
python storage_engine_demo.py
```

### 6. 使用示例
```bash
cd demo
python usage_examples.py
```

## 📚 核心代码说明

### src/ 目录
- **`lsm_tree.py`** - LSM-Tree基础实现
  - MemTable (内存表)
  - SSTable (有序字符串表)
  - Compaction (合并机制)
  - Bloom Filter (布隆过滤器)
  - 完整的测试用例和性能演示

- **`lsm_tree_v2.py`** - LSM-Tree V2 (支持多种存储后端)
  - 存储抽象接口
  - 支持Pickle、JSON、Excel、S3、内存存储
  - 动态存储后端切换
  - 完整的测试用例和演示

- **`lsm_tree_v3.py`** - LSM-Tree V3 (使用新的存储引擎包)
  - 模块化的存储引擎包
  - 自动注册机制
  - 更好的扩展性
  - 完整的测试用例和演示

- **`storage/`** - 存储引擎包
  - **`core/`** - 核心接口和工厂
  - **`backends/`** - 各种存储后端实现
  - 支持自动注册和发现
  - 易于扩展自定义存储后端

### demo/ 目录
- **`lsm_tree_guide.py`** - 详细学习指南
  - 核心概念解释
  - 写入放大演示
  - 读取性能分析
  - Compaction影响演示
  - 并发访问演示
  - 空间效率分析
  - 范围查询演示

- **`lsm_tree_visualizer.py`** - 可视化工具
  - MemTable flush过程可视化
  - Compaction过程可视化
  - 读取过程可视化
  - 空间使用情况可视化
  - 交互式演示模式

- **`storage_demo.py`** - 存储后端演示
  - 多种存储后端使用示例
  - 存储后端切换演示
  - 性能对比测试
  - 交互式演示模式

- **`storage_engine_demo.py`** - 存储引擎包演示
  - 存储注册表功能演示
  - 存储工厂模式演示
  - 自定义存储后端演示
  - 性能对比和上下文管理器演示

- **`usage_examples.py`** - 使用示例
  - 基本使用示例
  - 不同存储后端示例
  - 存储切换示例
  - 性能对比示例
  - 自定义存储示例

### data/ 目录
包含所有演示和测试生成的数据文件：
- **`*_demo/`** - 各种演示生成的数据
- **`*_data/`** - 测试数据
- **`*_visual/`** - 可视化数据
- **`*_example/`** - 示例数据

## 🎯 学习路径建议

1. **理解概念** - 先阅读 `lsm_tree_summary.md`
2. **运行测试** - 执行 `src/lsm_tree.py` 了解基本功能
3. **测试存储抽象** - 运行 `src/lsm_tree_v2.py` 了解存储抽象
4. **深入学习** - 运行 `demo/lsm_tree_guide.py` 学习各种特性
5. **可视化理解** - 使用 `demo/lsm_tree_visualizer.py` 直观理解工作原理
6. **实践应用** - 运行 `demo/usage_examples.py` 学习实际应用
7. **存储演示** - 运行 `demo/storage_demo.py` 了解存储后端

## ✨ 主要特性

- ✅ 完整的LSM-Tree实现
- ✅ MemTable和SSTable管理
- ✅ 自动Compaction机制
- ✅ 并发安全设计
- ✅ 性能测试和演示
- ✅ 详细的学习指南
- ✅ 可视化工具
- ✅ 实际应用场景分析
- ✅ 存储抽象接口
- ✅ 多种存储后端支持
- ✅ 动态存储切换
- ✅ 存储性能对比
- ✅ 清晰的目录结构

## 🎯 适用场景

- 写多读少的应用
- 日志系统
- 时序数据库
- 消息队列
- 缓存系统
- 键值存储引擎

## 🛠 技术栈

- Python 3.6+
- 多线程支持
- 文件系统操作
- 数据序列化 (pickle, json)
- Excel文件操作 (pandas, openpyxl)
- 云存储支持 (boto3)
- 性能测试工具

## 📖 文档

- **`lsm_tree_summary.md`** - 学习总结文档
  - LSM-Tree核心概念
  - 优势与劣势分析
  - 实际应用场景
  - 性能特点
  - 调优参数
  - 使用建议

通过这个完整的LSM-Tree实现，你可以深入理解现代数据库系统的核心存储技术！