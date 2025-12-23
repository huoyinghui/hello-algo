# Python刷题技巧手册

> 🐍 提升刷题效率的Python技巧与模块

---

## 1. 内置函数 🐍

### 1.1 map, filter, zip

```python
# map - 映射
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
# [1, 4, 9, 16]

# filter - 过滤
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
# [2, 4]

# zip - 并行迭代
pairs = list(zip([1, 2, 3], ['a', 'b', 'c']))
# [(1, 'a'), (2, 'b'), (3, 'c')]

# zip解包
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for a, b in zip(nums1, nums2):
    print(a, b)
```

---

### 1.2 enumerate, sorted, reversed

```python
# enumerate - 同时获取索引和值
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c

# enumerate指定起始索引
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(i, val)  # 1 a, 2 b, 3 c

# sorted - 排序（返回新列表）
sorted([3, 1, 4, 1, 5])  # [1, 1, 3, 4, 5]
sorted([3, 1, 4], reverse=True)  # [4, 3, 1]
sorted(['apple', 'pie', 'a'], key=len)  # ['a', 'pie', 'apple']

# 多关键字排序
points = [(1, 2), (3, 1), (1, 1)]
sorted(points, key=lambda x: (x[0], x[1]))

# reversed - 反转迭代器
list(reversed([1, 2, 3]))  # [3, 2, 1]
```

---

### 1.3 all, any, sum, max, min

```python
# all - 全部为True
all([True, True, False])  # False
all([1, 2, 3])  # True
all([])  # True (空列表)

# any - 任一为True
any([False, False, True])  # True
any([0, 0, 1])  # True
any([])  # False

# sum - 求和
sum([1, 2, 3, 4])  # 10
sum([1, 2, 3], 10)  # 16 (起始值10)

# max, min - 最大最小值
max([1, 5, 3])  # 5
min([1, 5, 3])  # 1
max('abc')  # 'c'
max([1, 2, 3], key=lambda x: -x)  # 1
```

---

## 2. collections 模块 🐍

### 2.1 Counter - 计数器

```python
from collections import Counter

# 统计频率
nums = [1, 1, 2, 3, 3, 3]
counter = Counter(nums)
# Counter({3: 3, 1: 2, 2: 1})

# 最常见的k个元素
counter.most_common(2)  # [(3, 3), (1, 2)]

# 字符串统计
s = "hello world"
char_count = Counter(s)
# Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Counter运算
c1 = Counter(['a', 'b', 'c'])
c2 = Counter(['a', 'b', 'd'])
c1 + c2  # 相加
c1 - c2  # 相减
c1 & c2  # 交集
c1 | c2  # 并集

# 实用技巧
counter['x']  # 不存在返回0，不报错
```

---

### 2.2 defaultdict - 默认字典

```python
from collections import defaultdict

# 默认值为int
count = defaultdict(int)
for num in [1, 2, 1, 3]:
    count[num] += 1  # 不用检查键是否存在
# defaultdict(<class 'int'>, {1: 2, 2: 1, 3: 1})

# 默认值为list
graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)
# defaultdict(<class 'list'>, {1: [2, 3]})

# 默认值为set
groups = defaultdict(set)
groups['A'].add(1)
groups['A'].add(2)

# 自定义默认值
d = defaultdict(lambda: 'N/A')
d['key']  # 'N/A'
```

---

### 2.3 deque - 双端队列

```python
from collections import deque

# 创建
dq = deque([1, 2, 3])

# 右端操作
dq.append(4)        # [1, 2, 3, 4]
dq.pop()            # 4, [1, 2, 3]

# 左端操作
dq.appendleft(0)    # [0, 1, 2, 3]
dq.popleft()        # 0, [1, 2, 3]

# 旋转
dq.rotate(1)        # [3, 1, 2] 向右旋转
dq.rotate(-1)       # [1, 2, 3] 向左旋转

# 限制长度
dq = deque(maxlen=3)
dq.extend([1, 2, 3, 4])  # deque([2, 3, 4], maxlen=3)
```

**应用场景：**
- BFS队列
- 滑动窗口
- 循环缓冲

---

## 3. heapq 模块 - 堆 🐍

```python
import heapq

# 小顶堆
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
min_val = heapq.heappop(heap)  # 1

# 批量建堆
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)  # O(n) 原地建堆

# Top K问题
heapq.nlargest(3, nums)    # [9, 6, 5]
heapq.nsmallest(3, nums)   # [1, 1, 2]

# 大顶堆（使用负数）
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
max_val = -heapq.heappop(max_heap)  # 3

# 堆排序
def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

# 合并有序序列
merged = heapq.merge([1, 3, 5], [2, 4, 6])
# [1, 2, 3, 4, 5, 6]
```

**典型应用：**
- LeetCode 215. 数组中的第K个最大元素
- LeetCode 23. 合并K个升序链表
- LeetCode 347. 前K个高频元素

---

## 4. bisect 模块 - 二分查找 🐍

```python
import bisect

nums = [1, 3, 5, 7, 9]

# bisect_left - 查找插入位置（左边界）
pos = bisect.bisect_left(nums, 5)   # 2
pos = bisect.bisect_left(nums, 6)   # 3

# bisect_right - 查找插入位置（右边界）
pos = bisect.bisect_right(nums, 5)  # 3
pos = bisect.bisect(nums, 5)        # 同bisect_right

# insort - 插入并保持有序
bisect.insort(nums, 4)  # [1, 3, 4, 5, 7, 9]
bisect.insort_left(nums, 5)
bisect.insort_right(nums, 5)

# 应用：查找区间
def count_range(nums, left, right):
    """统计[left, right]范围内的元素个数"""
    l = bisect.bisect_left(nums, left)
    r = bisect.bisect_right(nums, right)
    return r - l
```

---

## 5. itertools 模块 🐍

```python
from itertools import *

# combinations - 组合 C(n, k)
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

# permutations - 排列 A(n, k)
list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# product - 笛卡尔积
list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# accumulate - 累积（前缀和）
list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]
list(accumulate([1, 2, 3, 4], lambda x, y: x * y))  # [1, 2, 6, 24]

# chain - 连接多个迭代器
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# islice - 切片迭代器
list(islice([1, 2, 3, 4, 5], 2, 4))  # [3, 4]

# groupby - 分组
from itertools import groupby
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

---

## 6. 常用代码片段 🔥

```python
# 1. 二维数组初始化
dp = [[0] * n for _ in range(m)]  # ✅ 正确
dp = [[0] * n] * m                # ❌ 浅拷贝，错误！

# 2. 无穷大/无穷小
INF = float('inf')
NEG_INF = float('-inf')

# 3. 字符与ASCII码互转
ord('a')  # 97
chr(97)   # 'a'

# 4. 字符串反转
s = "hello"
s[::-1]  # "olleh"

# 5. 列表去重（保持顺序）
def dedupe(nums):
    seen = set()
    return [x for x in nums if not (x in seen or seen.add(x))]

# 列表去重（不保持顺序）
list(set(nums))

# 6. 字典按值排序
d = {'a': 3, 'b': 1, 'c': 2}
sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]

# 7. 多变量赋值
a, b = b, a  # 交换
a, b, c = 1, 2, 3

# 8. 判断奇偶
is_odd = (n & 1) == 1
is_even = (n & 1) == 0

# 9. 整数除法（向下取整）
7 // 2  # 3
-7 // 2  # -4

# 10. 进制转换
bin(10)  # '0b1010' 二进制
oct(10)  # '0o12' 八进制
hex(10)  # '0xa' 十六进制

# 11. 列表推导式
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
matrix = [[0] * n for _ in range(m)]

# 12. 字典推导式
{k: v for k, v in items if condition}
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 13. 集合推导式
{x for x in nums if x > 0}

# 14. 生成器表达式
gen = (x**2 for x in range(10))  # 节省内存
```

---

## 7. Python位运算技巧

```python
# 判断奇偶
n & 1 == 1  # 奇数

# 乘以/除以2的幂
n << 1  # n * 2
n >> 1  # n // 2

# 交换两个数
a ^= b
b ^= a
a ^= b

# 判断是否为2的幂
n > 0 and (n & (n - 1)) == 0

# 获取最低位的1
n & -n

# 去掉最低位的1
n & (n - 1)

# 统计1的个数
bin(n).count('1')
```

---

## 8. 字符串技巧

```python
# join拼接（比+快）
''.join(['a', 'b', 'c'])  # 'abc'
' '.join(['hello', 'world'])  # 'hello world'

# split分割
'a,b,c'.split(',')  # ['a', 'b', 'c']
'hello  world'.split()  # ['hello', 'world']

# f-string格式化
name, age = 'Alice', 20
f'{name} is {age} years old'

# 字符串乘法
'ab' * 3  # 'ababab'

# in运算符
'hello' in 'hello world'  # True

# 字符串切片
s = 'hello'
s[::-1]  # 'olleh' 反转
s[::2]   # 'hlo' 间隔
s[1:4]   # 'ell' 子串
```

---

## 9. 常用一行代码

```python
# 展平二维列表
flat = [item for sublist in matrix for item in sublist]

# 转置矩阵
transposed = list(zip(*matrix))

# 查找列表中的最大/最小索引
max_idx = max(range(len(nums)), key=lambda i: nums[i])
min_idx = min(range(len(nums)), key=lambda i: nums[i])

# 去除列表中的None
[x for x in lst if x is not None]

# 列表元素计数
from collections import Counter
Counter(nums)

# 快速幂
pow(2, 10)  # 1024
pow(2, 10, 1000)  # 24 (2^10 % 1000)
```

---

## 10. 性能优化技巧

```python
# 1. 使用局部变量（比全局变量快）
def func():
    local_var = global_var  # 缓存到局部

# 2. 使用set而非list判断存在
if x in some_set:  # O(1)
if x in some_list:  # O(n)

# 3. 列表推导式比循环快
[x**2 for x in range(100)]  # 快
result = []
for x in range(100):
    result.append(x**2)  # 慢

# 4. join比+拼接字符串快
''.join(str_list)  # 快
result = ''
for s in str_list:
    result += s  # 慢

# 5. 使用内置函数
sum(nums)  # 快
total = 0
for n in nums:
    total += n  # 慢
```

---

## 🔗 相关文件

- 📦 [数据结构模板](./01-数据结构模板.md)
- 💎 [动态规划模板](./04-动态规划模板.md)
- 📋 [必刷题目清单](../practice/必刷题目清单.md)

**🎯 熟练掌握这些技巧，刷题事半功倍！**
