# 第3天：哈希表与树

## 📚 学习目标
掌握哈希表的原理和实现，理解二叉树的概念和遍历方法，为后续学习高级数据结构打下基础。

## 🔍 核心知识点

### 上午：哈希表（Hash Table）

#### 1. 哈希表基础概念
- **定义**：通过键值对（key-value）存储数据的数据结构
- **核心思想**：通过哈希函数将键映射到数组索引
- **优点**：
  - 理想情况下查找、插入、删除都是O(1)
  - 适合频繁查找的场景

#### 2. 哈希函数
- **作用**：将任意大小的输入映射到固定大小的输出
- **特性**：
  - 确定性：相同输入产生相同输出
  - 均匀性：均匀分布到哈希表空间
  - 高效性：计算快速

#### 3. 哈希冲突处理
- **链地址法（Separate Chaining）**：
  - 每个桶维护一个链表
  - 冲突元素添加到链表

- **开放寻址法（Open Addressing）**：
  - 线性探测：向后查找空位
  - 二次探测：平方步长探测
  - 双重哈希：使用第二个哈希函数

#### 4. 必须掌握的操作
```python
class HashMap:
    def __init__(self):             # 初始化
    def put(self, key, value):      # 插入键值对
    def get(self, key):             # 获取值
    def remove(self, key):          # 删除键值对
    def contains_key(self, key):    # 判断键是否存在
    def hash_function(self, key):   # 哈希函数
```

### 下午：树（Tree）

#### 1. 树的基础概念
- **定义**：由节点和边组成的层次结构
- **基本术语**：
  - 节点、根节点、父节点、子节点
  - 叶子节点、度、深度、高度
  - 层、兄弟节点、堂兄弟节点

#### 2. 二叉树（Binary Tree）
- **定义**：每个节点最多有两个子节点的树
- **性质**：
  - 第i层最多有2^(i-1)个节点
  - 深度为k的二叉树最多有2^k-1个节点
  - 叶子节点数 = 度为2的节点数 + 1

#### 3. 二叉树的遍历
- **深度优先遍历（DFS）**：
  - 前序遍历：根-左-右
  - 中序遍历：左-根-右
  - 后序遍历：左-右-根

- **广度优先遍历（BFS）**：
  - 层序遍历：逐层从左到右

#### 4. 二叉搜索树（BST）
- **定义**：满足以下性质的二叉树：
  - 左子树所有节点 < 根节点
  - 右子树所有节点 > 根节点
  - 左右子树都是二叉搜索树

- **操作**：
  - 查找：O(log n) 平均，O(n) 最坏
  - 插入：保持BST性质
  - 删除：三种情况处理

## 📁 相关代码文件
- 哈希表：
  - `codes/python/chapter_hashing/hash_map.py`
  - `codes/go/chapter_hashing/hash_map.go`
- 树：
  - `codes/python/chapter_tree/binary_tree.py`
  - `codes/python/chapter_tree/binary_search_tree.py`
  - `codes/go/chapter_tree/`

## 📖 推荐阅读文档
- `docs/chapter_hashing/`
- `docs/chapter_tree/`

## 💻 动手实践

### 练习1：实现哈希表（链地址法）
要求：
1. 设计合适的哈希函数
2. 实现扩容机制
3. 处理哈希冲突

### 练习2：实现二叉树
要求：
1. 定义二叉树节点
2. 实现三种深度优先遍历
3. 实现层序遍历

### 练习3：实现二叉搜索树
要求：
1. 实现BST的插入操作
2. 实现BST的查找操作
3. 实现BST的删除操作（三种情况）

### 练习4：哈希表应用
要求：
1. 实现一个简单的缓存系统
2. 使用哈希表优化查找效率

## 🎯 晚上刷题（LeetCode）

### 哈希表类题目
1. **[1. 两数之和](https://leetcode.cn/problems/two-sum/)**
   - 难度：简单
   - 考点：哈希表查找优化

2. **[3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)**
   - 难度：中等
   - 考点：滑动窗口+哈希表

3. **[128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/)**
   - 难度：中等
   - 考点：哈希集合应用

4. **[49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)**
   - 难度：中等
   - 考点：哈希表分组

### 二叉树类题目
1. **[94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)**
   - 难度：简单
   - 考点：递归/迭代遍历

2. **[144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)**
   - 难度：简单
   - 考点：遍历基础

3. **[145. 二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/)**
   - 难度：简单
   - 考点：遍历基础

4. **[102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)**
   - 难度：中等
   - 考点：BFS遍历

5. **[104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)**
   - 难度：简单
   - 考点：递归/层序遍历

6. **[101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)**
   - 难度：简单
   - 考点：递归判断

## ✅ 掌握标准
- [ ] 理解哈希表的工作原理和哈希冲突处理
- [ ] 能手动实现一个哈希表
- [ ] 掌握二叉树的基本概念和遍历方法
- [ ] 能实现二叉搜索树及其基本操作
- [ ] 熟悉树相关的递归思想
- [ ] 能解决LeetCode中等难度的哈希表/树题目

## 📝 学习笔记
### 重点记录
1. 哈希函数设计要点
2. 装载因子与扩容的关系
3. 二叉树遍历的递归和非递归实现
4. BST操作的时间复杂度分析
5. 递归问题的解决思路

### 常见错误
1. 哈希冲突处理不当
2. 扩容时机选择不合理
3. 二叉树遍历的边界条件
4. BST删除时的指针处理
5. 递归终止条件设置错误

### 实用技巧
1. 哈希表优化查找类问题
2. 使用字典统计频率
3. 树的递归三部曲：确定参数、确定终止条件、确定单层逻辑
4. BFS使用队列辅助实现
5. 迭代遍历使用栈辅助实现