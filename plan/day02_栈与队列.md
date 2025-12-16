# 第2天：栈与队列

## 📚 学习目标
掌握栈和队列的原理、实现和应用场景，能够灵活运用解决实际问题。

## 🔍 核心知识点

### 上午：栈（Stack）

#### 1. 栈的基础概念
- **定义**：后进先出（LIFO）的线性数据结构
- **类比**：像一叠盘子，只能从顶部取放
- **特性**：
  - 只在栈顶操作
  - push/pop操作：O(1)时间复杂度

#### 2. 栈的实现方式
- **基于数组**：顺序栈
  - 优点：实现简单，缓存友好
  - 缺点：需要预先分配空间

- **基于链表**：链式栈
  - 优点：动态大小，无容量限制
  - 缺点：需要额外空间存储指针

#### 3. 必须掌握的操作
```python
class Stack:
    def __init__(self):             # 初始化
    def push(self, item):           # 入栈
    def pop(self):                  # 出栈
    def peek(self):                 # 查看栈顶元素
    def is_empty(self):             # 判断是否为空
    def size(self):                 # 获取栈大小
```

### 下午：队列（Queue）

#### 1. 队列的基础概念
- **定义**：先进先出（FIFO）的线性数据结构
- **类比**：像排队买票，先来先服务
- **特性**：
  - 在队尾入队，队头出队
  - enqueue/dequeue操作：O(1)时间复杂度

#### 2. 队列的实现方式
- **基于数组**：
  - 普通数组实现：出队时需要移动元素
  - 循环数组：使用模运算实现循环利用

- **基于链表**：
  - 维护头尾两个指针
  - 入队在尾部，出队在头部

#### 3. 必须掌握的操作
```python
class Queue:
    def __init__(self):             # 初始化
    def enqueue(self, item):        # 入队
    def dequeue(self):              # 出队
    def front(self):                # 查看队头元素
    def is_empty(self):             # 判断是否为空
    def size(self):                 # 获取队列大小
```

#### 4. 双端队列（Deque）
- **定义**：两端都可以进行插入和删除的队列
- **操作**：头插/尾插，头删/尾删
- **应用**：滑动窗口、回文检查

## 📁 相关代码文件
- Python实现：
  - `codes/python/chapter_stack_and_queue/stack.py`
  - `codes/python/chapter_stack_and_queue/queue.py`
  - `codes/python/chapter_stack_and_queue/deque.py`
- Go实现：
  - `codes/go/chapter_stack_and_queue/`
  - `codes/go/chapter_stack_and_queue/deque.go`

## 📖 推荐阅读文档
- `docs/chapter_stack_and_queue/`

## 💻 动手实践

### 练习1：实现栈（数组版本）
要求：
1. 实现基本的栈操作
2. 处理栈满时的扩容
3. 异常处理（空栈pop）

### 练习2：实现栈（链表版本）
要求：
1. 使用链表节点实现
2. 体会与数组版本的区别

### 练习3：实现循环队列
要求：
1. 使用数组实现循环队列
2. 正确处理队满和队空的判断
3. 实现队列的所有基本操作

### 练习4：实现双端队列
要求：
1. 支持两端的插入删除
2. 考虑不同底层数据结构的选择

## 🎯 晚上刷题（LeetCode）

### 栈类题目
1. **[20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/)**
   - 难度：简单
   - 考点：栈的基本应用、配对检查

2. **[155. 最小栈](https://leetcode.cn/problems/min-stack/)**
   - 难度：中等
   - 考点：辅助栈、栈的设计

3. **[394. 字符串解码](https://leetcode.cn/problems/decode-string/)**
   - 难度：中等
   - 考点：栈的嵌套使用

4. **[739. 每日温度](https://leetcode.cn/problems/daily-temperatures/)**
   - 难度：中等
   - 考点：单调栈

### 队列类题目
1. **[225. 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/)**
   - 难度：简单
   - 考点：数据结构间的转换

2. **[232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)**
   - 难度：简单
   - 考点：双栈技巧

3. **[239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)**
   - 难度：困难
   - 考点：单调队列

4. **[622. 设计循环队列](https://leetcode.cn/problems/design-circular-queue/)**
   - 难度：中等
   - 考点：循环队列实现

## ✅ 掌握标准
- [ ] 能清晰说明栈和队列的特性和区别
- [ ] 能用数组和链表两种方式实现栈和队列
- [ ] 能实现循环队列并正确处理边界
- [ ] 理解双端队列的应用场景
- [ ] 能熟练解决LeetCode中等难度的栈/队列题目
- [ ] 掌握单调栈和单调队列的思想

## 📝 学习笔记
### 重点记录
1. 栈的LIFO和队列的FIFO特性在实际问题中的应用
2. 循环队列的实现技巧（队满队空判断）
3. 两个栈实现队列的思路
4. 单调栈/单调队列的原理和应用

### 常见错误
1. 循环队列的边界条件处理错误
2. 栈空/队空时的异常处理
3. 队列基于数组实现时的效率问题
4. 忘记更新头尾指针

### 实用技巧
1. 用栈处理括号匹配、表达式求值
2. 用队列处理层序遍历、BFS
3. 单调栈处理下一个更大/更小元素
4. 双端队列处理滑动窗口问题