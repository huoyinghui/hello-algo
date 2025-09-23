# LSM-Tree 实现和学习资源

这个目录包含了完整的LSM-Tree (Log-Structured Merge-Tree) 实现和学习资源。

## 文件说明

### 核心实现
- **`lsm_tree.py`** - LSM-Tree的完整实现
  - MemTable (内存表)
  - SSTable (有序字符串表)
  - Compaction (合并机制)
  - Bloom Filter (布隆过滤器)
  - 完整的测试用例和性能演示

### 学习资源
- **`lsm_tree_guide.py`** - 详细的学习指南
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

- **`lsm_tree_summary.md`** - 学习总结文档
  - LSM-Tree核心概念
  - 优势与劣势分析
  - 实际应用场景
  - 性能特点
  - 调优参数
  - 使用建议

## 快速开始

### 1. 运行基本测试
```bash
cd lsm
python lsm_tree.py
```

### 2. 学习核心概念
```bash
python lsm_tree_guide.py
```

### 3. 可视化演示
```bash
python lsm_tree_visualizer.py
```

## 学习路径建议

1. **理解概念** - 先阅读 `lsm_tree_summary.md`
2. **运行测试** - 执行 `lsm_tree.py` 了解基本功能
3. **深入学习** - 运行 `lsm_tree_guide.py` 学习各种特性
4. **可视化理解** - 使用 `lsm_tree_visualizer.py` 直观理解工作原理
5. **实践应用** - 基于代码实现自己的LSM-Tree应用

## 主要特性

- ✅ 完整的LSM-Tree实现
- ✅ MemTable和SSTable管理
- ✅ 自动Compaction机制
- ✅ 并发安全设计
- ✅ 性能测试和演示
- ✅ 详细的学习指南
- ✅ 可视化工具
- ✅ 实际应用场景分析

## 适用场景

- 写多读少的应用
- 日志系统
- 时序数据库
- 消息队列
- 缓存系统
- 键值存储引擎

## 技术栈

- Python 3.6+
- 多线程支持
- 文件系统操作
- 数据序列化 (pickle)
- 性能测试工具

通过这个完整的LSM-Tree实现，你可以深入理解现代数据库系统的核心存储技术！
