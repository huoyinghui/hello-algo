# 第1天：数组与链表

## 📚 学习目标
掌握数组和链表的基本概念、操作和实现，能够手写代码解决相关问题。

## 🔍 核心知识点

### 上午：数组（Array）

#### 1. 数组基础概念
- **定义**：连续内存空间存储相同类型数据的线性数据结构
- **特性**：
  - 随机访问：O(1) 时间复杂度
  - 插入/删除：O(n) 时间复杂度
  - 空间局部性好，缓存友好

#### 2. 静态数组
- **固定大小**：创建后长度不可改变
- **内存分配**：栈或堆上的连续内存
- **应用场景**：已知数据量，查询频繁

#### 3. 动态数组
- **可扩容**：自动调整数组大小
- **实现原理**：
  - 初始容量设定
  - 扩容策略（通常2倍）
  - 数据复制迁移

#### 4. 必须掌握的操作
```python
# Python版需要掌握的方法
class MyArray:
    def __init__(self, capacity):      # 初始化
    def get(self, index):              # 获取元素
    def set(self, index, value):       # 设置元素
    def append(self, value):           # 尾部添加
    def insert(self, index, value):    # 指定位置插入
    def remove(self, index):           # 删除元素
    def resize(self):                  # 扩容
```

### 下午：链表（Linked List）

#### 1. 链表基础概念
- **定义**：通过指针连接的离散节点序列
- **特性**：
  - 动态大小：运行时改变
  - 插入/删除：O(1) （已知位置）
  - 随机访问：O(n)

#### 2. 单链表
- **节点结构**：数据域 + 后继指针
- **头节点**：便于操作的哑节点
- **尾节点**：后继指针为NULL

#### 3. 双链表
- **节点结构**：数据域 + 前驱指针 + 后继指针
- **优势**：双向遍历，某些操作更高效

#### 4. 必须掌握的操作
```python
# Python版需要掌握的方法
class ListNode:
    def __init__(self, val=0, next=None):  # 节点定义

class MyLinkedList:
    def __init__(self):              # 初始化
    def get(self, index):            # 获取元素
    def add_at_head(self, val):      # 头部添加
    def add_at_tail(self, val):      # 尾部添加
    def add_at_index(self, index, val):  # 指定位置添加
    def delete_at_index(self, index):    # 删除节点
```

## 📁 相关代码文件
- Python实现：
  - `codes/python/chapter_array_and_linkedlist/array.py`
  - `codes/python/chapter_array_and_linkedlist/linked_list.py`
- Go实现：
  - `codes/go/chapter_array_and_linkedlist/array.go`
  - `codes/go/chapter_array_and_linkedlist/linked_list.go`

## 📖 推荐阅读文档
- `docs/chapter_array_and_linkedlist/`

## 💻 动手实践

### 练习1：实现动态数组
要求：
1. 实现基本的增删改查
2. 实现自动扩容机制
3. 处理边界情况（空数组、越界访问）

### 练习2：实现单链表
要求：
1. 实现完整的增删改查
2. 使用虚拟头节点简化操作
3. 正确处理各种边界情况

### 练习3：实现双链表
要求：
1. 在单链表基础上实现
2. 体会双链表在某些场景的优势

## 🎯 晚上刷题（LeetCode）

### 数组类题目
1. **[1. 两数之和](https://leetcode.cn/problems/two-sum/)**
   - 难度：简单
   - 考点：数组遍历、哈希表优化

2. **[4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/)**
   - 难度：困难
   - 考点：数组合并、二分查找

3. **[27. 移除元素](https://leetcode.cn/problems/remove-element/)**
   - 难度：简单
   - 考点：双指针、原地修改

### 链表类题目
1. **[206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)**
   - 难度：简单
   - 考点：迭代/递归、指针操作

2. **[21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)**
   - 难度：简单
   - 考点：双指针、链表合并

3. **[234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/)**
   - 难度：简单
   - 考点：快慢指针、链表反转

## ✅ 掌握标准
- [ ] 能清晰说明数组和链表的区别和应用场景
- [ ] 能不参考文档手写实现动态数组
- [ ] 能不参考文档手写实现单链表和双链表
- [ ] 能熟练解决LeetCode中等难度的数组/链表题目
- [ ] 理解时间复杂度和空间复杂度的分析

## 📝 学习笔记
### 重点记录
1. 数组扩容的具体过程和时间复杂度分析
2. 链表操作中的边界情况处理技巧
3. 虚拟头节点的使用场景和优势
4. 快慢指针等常用技巧

### 常见错误
1. 链表操作时的指针丢失
2. 忘记处理空链表情况
3. 数组越界访问
4. 内存泄漏（Go语言的nil处理）