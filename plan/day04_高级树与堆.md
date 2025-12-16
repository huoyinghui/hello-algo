# 第4天：高级树结构与堆

## 📚 学习目标
掌握AVL树的自平衡原理、堆的概念和应用，理解优先队列的实现，并能解决相关的算法问题。

## 🔍 核心知识点

### 上午：AVL树（平衡二叉搜索树）

#### 1. AVL树基础概念
- **定义**：自平衡的二叉搜索树
- **发明者**：Adelson-Velsky 和 Landis（1962年）
- **平衡因子**：左子树高度 - 右子树高度（只可能是-1, 0, 1）
- **特性**：
  - 任何节点的两个子树的高度差不超过1
  - 查找、插入、删除都是O(log n)

#### 2. 树的旋转操作
- **左旋（Left Rotation）**：
  - 右子树过高时使用
  - 将右子节点提升为新的根

- **右旋（Right Rotation）**：
  - 左子树过高时使用
  - 将左子节点提升为新的根

- **左右旋（Left-Right Rotation）**：
  - 先左旋后右旋
  - 处理LR不平衡情况

- **右左旋（Right-Left Rotation）**：
  - 先右旋后左旋
  - 处理RL不平衡情况

#### 3. AVL树的插入
1. 按BST规则插入节点
2. 更新路径上所有节点的高度
3. 检查平衡因子
4. 若不平衡，进行相应旋转

#### 4. AVL树的删除
1. 按BST规则删除节点
2. 更新高度并检查平衡
3. 从删除位置向上回溯，调整平衡

### 下午：堆（Heap）

#### 1. 堆的基础概念
- **定义**：完全二叉树，满足堆属性
- **完全二叉树**：除最后一层外都是满的，最后一层从左到右填充
- **堆属性**：
  - 最大堆：父节点 >= 子节点
  - 最小堆：父节点 <= 子节点

#### 2. 堆的数组表示
- **索引关系**（从0开始）：
  - 父节点：i -> (i-1)//2
  - 左子节点：i -> 2*i+1
  - 右子节点：i -> 2*i+2

#### 3. 堆的核心操作
- **堆化（Heapify）**：
  - 向上调整（Sift Up）：用于插入
  - 向下调整（Sift Down）：用于删除

- **建堆（Build Heap）**：
  - 方法1：逐个插入O(n log n)
  - 方法2：原地建堆O(n)

#### 4. 堆的操作
```python
class MaxHeap:
    def __init__(self):             # 初始化
    def insert(self, val):          # 插入元素
    def extract_max(self):          # 提取最大值
    def peek(self):                 # 查看堆顶
    def size(self):                 # 获取大小
    def heapify_up(self, index):    # 向上调整
    def heapify_down(self, index):  # 向下调整
```

## 📁 相关代码文件
- AVL树：
  - `codes/python/chapter_tree/avl_tree.py`
  - `codes/go/chapter_tree/avl_tree.go`
- 堆：
  - `codes/python/chapter_heap/heap.py`
  - `codes/go/chapter_heap/heap.go`

## 📖 推荐阅读文档
- `docs/chapter_tree/avl_tree.md`
- `docs/chapter_heap/`

## 💻 动手实践

### 练习1：实现AVL树
要求：
1. 实现节点的定义（包含高度字段）
2. 实现四种旋转操作
3. 实现插入时的平衡调整
4. 实现删除时的平衡调整

### 练习2：实现最大堆
要求：
1. 使用数组实现
2. 实现插入和提取操作
3. 实现堆化操作
4. 实现建堆操作

### 练习3：堆排序
要求：
1. 使用堆实现排序算法
2. 理解原地堆排序的过程
3. 分析时间复杂度和空间复杂度

### 练习4：优先队列
要求：
1. 使用堆实现优先队列
2. 支持优先级的动态修改
3. 实现高效的删除操作

## 🎯 晚上刷题（LeetCode）

### AVL树相关题目
1. **[1382. 将二叉搜索树变平衡](https://leetcode.cn/problems/balance-a-binary-search-tree/)**
   - 难度：中等
   - 考点：BST平衡化

### 堆类题目
1. **[215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)**
   - 难度：中等
   - 考点：堆的应用、Top K问题

2. **[23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)**
   - 难度：困难
   - 考点：优先队列、堆的应用

3. **[347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)**
   - 难度：中等
   - 考点：哈希表+堆

4. **[295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/)**
   - 难度：困难
   - 考点：双堆技巧

5. **[264. 丑数 II](https://leetcode.cn/problems/ugly-number-ii/)**
   - 难度：中等
   - 考点：最小堆、动态规划

6. **[692. 前K个高频单词](https://leetcode.cn/problems/top-k-frequent-words/)**
   - 难度：中等
   - 考点：堆+自定义比较

## ✅ 掌握标准
- [ ] 理解AVL树的平衡原理和旋转操作
- [ ] 能手动实现AVL树的插入和删除
- [ ] 掌握堆的概念和数组表示方法
- [ ] 能实现最大堆和最小堆
- [ ] 理解堆排序的过程
- [ ] 能运用堆解决Top K类问题
- [ ] 掌握双堆技巧解决中位数问题

## 📝 学习笔记
### 重点记录
1. AVL树的四种旋转场景和判断方法
2. 堆的数组表示索引关系
3. 向上堆化和向下堆化的实现细节
4. 建堆的两种方法及其复杂度分析
5. 堆在解决实际问题中的应用模式

### 常见错误
1. AVL树旋转后的子树连接错误
2. 忘记更新旋转后的高度
3. 堆化过程中的索引计算错误
4. 堆排序时忘记调整堆的大小
5. 双堆技巧的边界条件处理

### 实用技巧
1. 记住旋转的口诀："左旋看右，右旋看左"
2. 堆的父子节点关系公式
3. 使用堆的典型场景：Top K、中位数、合并有序序列
4. 小顶堆找最大，大顶堆找最小
5. Python中的heapq模块使用技巧

### 进阶思考
1. 为什么完全二叉树适合用数组表示？
2. AVL树和红黑树的对比
3. 堆和BST的适用场景区别
4. 如何设计一个支持删除任意元素的堆？