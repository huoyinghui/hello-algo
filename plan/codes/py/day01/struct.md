
## Python 常用数据结构

类似于 C++ STL，Python 也提供了一整套常用数据结构（实际底层细节可能因实现而异）。下面结合简单 demo，帮助快速上手。

### 1. 序列容器（Sequence Containers）

#### list：动态数组

- 适合频繁随机访问，`O(1)` 读取、尾部增删。
- 常用来保存中间结果，也可以当作栈使用。

**示例**

```python
nums = [1, 2, 3]
nums.append(4)          # 尾部插入 O(1)
print(nums[0])          # 随机访问 O(1) -> 1
print(nums)             # [1, 2, 3, 4]

# 作为栈使用
nums.append(5)
top = nums.pop()        # 弹出栈顶（尾部）
print(top, nums)        # 5 [1, 2, 3, 4]
```

#### tuple：不可变序列

- `tuple` 是不可变的 `list`，长度与元素都不能修改。
- 适合存放“只读”的数据，如坐标、配置等。

**示例**

```python
point = (1, 2)
x, y = point
print(x, y)             # 1 2

# point[0] = 3          # TypeError：tuple 不可修改
```

#### collections.deque：双端队列

- 支持在两端 `O(1)` 插入与删除，可作为队列或双端队列。
- 也支持下标访问，适合实现滑动窗口、单调队列等。

**示例**

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)        # 头部插入
dq.append(4)            # 尾部插入
print(dq)               # deque([0, 1, 2, 3, 4])

print(dq.popleft())     # 0，头部弹出
print(dq.pop())         # 4，尾部弹出
print(dq[0])            # 剩余队首元素
```

### 2. 容器适配器（Container Adaptors）

#### heapq：最小堆

- 基于 `list` 实现最小堆，适合维护一批数据中的最小值或前 K 小。
- `heapq.heapify`：`O(n)` 建堆；`heappush/heappop`：`O(log n)`。

**示例：取数组中最小的两个数**

```python
import heapq

nums = [5, 1, 3, 2, 4]
heapq.heapify(nums)         # 原地建堆

print(nums[0])              # 当前最小值 -> 1

min1 = heapq.heappop(nums)  # 取出最小值
min2 = heapq.heappop(nums)  # 取出次小值
print(min1, min2)           # 1 2
```

**示例：自定义比较（用 tuple 存 (key, index)）**

```python
import heapq

nums = [5, 1, 3]
heap = []

for i, x in enumerate(nums):
    # 按绝对值排序，相同绝对值按下标排序
    heapq.heappush(heap, (abs(x), i, x))

print(heapq.heappop(heap))  # (1, 1, 1)
```

### 3. 有序关联容器（Ordered Associative Containers）

#### collections.OrderedDict：按插入顺序的字典

- 按插入顺序记录 key，适合实现 LRU 等“最近使用”逻辑。

**示例：简单 LRU 思路**

```python
from collections import OrderedDict

cache = OrderedDict()

def put(key, value):
    if key in cache:
        cache.move_to_end(key)   # 使用后挪到末尾
    cache[key] = value
    if len(cache) > 2:           # 容量为 2
        cache.popitem(last=False)  # 弹出最旧的

def get(key):
    if key not in cache:
        return None
    cache.move_to_end(key)
    return cache[key]

put("a", 1)
put("b", 2)
print(list(cache.keys()))   # ['a', 'b']
get("a")
put("c", 3)
print(list(cache.keys()))   # ['a', 'c']，'b' 被淘汰
```

### 4. 无序关联容器（Unordered Associative Containers）

#### set：哈希集合

- 支持 `O(1)` 插入、删除、查找。
- 常用于“去重”和“快速判断某元素是否出现过”。

**示例**

```python
seen = set()
nums = [1, 2, 2, 3]

for x in nums:
    if x in seen:
        print("重复：", x)
    else:
        seen.add(x)
```

#### dict：哈希映射（哈希表）

- 以 `key -> value` 形式存储映射关系。
- 若 `key` 范围已知且较小，也可以用 `list` 下标代替 `dict`。

**示例：统计字符频次（dict 版本）**

```python
s = "abac"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)    # {'a': 2, 'b': 1, 'c': 1}
```

**示例：key 范围较小时用 list 代替**

```python
# 假设字符只可能是 0~9
counts = [0] * 10
digits = "012345"

for ch in digits:
    idx = ord(ch) - ord("0")
    counts[idx] += 1

print(counts)  # 每个数字出现次数
```

#### collections.Counter：计数器

- `Counter` 是 `dict` 的一个子类，专门做“元素计数”。
- 可以直接传入 `list` 或字符串，自动统计频次；支持 `most_common` 等方法。

**示例**

```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)

print(counter[2])              # 2 出现了 2 次
print(counter.most_common(2))  # 出现次数最多的两个元素
```

### 小结

理解这些常用数据结构的特点与适用场景，再配合上面的小 demo，能帮助你在刷题时更快地选择合适的数据结构，写出更简洁高效的代码。
