# 🐍 Python刷题常用模板

> 背会这些模板,刷题效率提升10倍！

---

## 📖 目录

1. [数据结构](#一数据结构)
2. [排序算法](#二排序算法)
3. [搜索算法](#三搜索算法)
4. [动态规划](#四动态规划)
5. [图论算法](#五图论算法)
6. [Python技巧](#六python技巧)

---

## 一、数据结构

### 1.1 链表节点

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 1.2 二叉树节点

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 1.3 并查集🔥

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        # 按秩合并
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
```

### 1.4 前缀树 Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
```

---

## 二、排序算法

### 2.1 快速排序🔥

```python
def quick_sort(nums, left, right):
    if left >= right:
        return
    
    pivot_idx = partition(nums, left, right)
    quick_sort(nums, left, pivot_idx - 1)
    quick_sort(nums, pivot_idx + 1, right)

def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i
```

### 2.2 归并排序

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## 三、搜索算法

### 3.1 二分查找🔥

```python
# 基础二分
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 左边界
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# 右边界
def upper_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1
```

### 3.2 DFS 深度优先搜索

```python
# 递归版
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 迭代版
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### 3.3 BFS 广度优先搜索🔥

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## 四、动态规划

### 4.1 记忆化搜索🐍

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(n):
    if n <= 1:
        return n
    return dp(n-1) + dp(n-2)
```

### 4.2 0-1背包🔥

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if w >= weights[i-1]:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w-weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# 空间优化🐍
def knapsack_01_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[capacity]
```

### 4.3 完全背包

```python
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[capacity]
```

### 4.4 最长递增子序列🔥

```python
import bisect

def length_of_lis(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

---

## 五、图论算法

### 5.1 拓扑排序🔥

```python
from collections import deque, defaultdict

def topological_sort(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []
```

### 5.2 Dijkstra最短路径🔥

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist
```

---

## 六、Python技巧

### 6.1 内置函数🐍

```python
# map, filter, zip
squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
pairs = list(zip(list1, list2))

# enumerate, sorted
for i, val in enumerate(nums):
    pass

sorted_nums = sorted(nums, key=lambda x: abs(x))
```

### 6.2 collections模块🐍

```python
from collections import Counter, defaultdict, deque

# Counter
counter = Counter(nums)
most_common = counter.most_common(k)

# defaultdict
graph = defaultdict(list)
graph[1].append(2)

# deque
dq = deque()
dq.append(x)       # 右端
dq.appendleft(x)   # 左端
dq.pop()           # 右端
dq.popleft()       # 左端
```

### 6.3 heapq模块🐍

```python
import heapq

# 小顶堆
heap = []
heapq.heappush(heap, 3)
min_val = heapq.heappop(heap)

# 批量建堆
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)

# TopK
largest_k = heapq.nlargest(k, nums)
smallest_k = heapq.nsmallest(k, nums)

# 大顶堆（用负数）
max_heap = []
heapq.heappush(max_heap, -x)
max_val = -heapq.heappop(max_heap)
```

### 6.4 bisect模块🐍

```python
import bisect

nums = [1, 3, 5, 7]

# 查找插入位置
pos_left = bisect.bisect_left(nums, 5)   # 2
pos_right = bisect.bisect_right(nums, 5)  # 3

# 插入并保持有序
bisect.insort(nums, 4)  # [1, 3, 4, 5, 7]
```

### 6.5 itertools模块🐍

```python
from itertools import combinations, permutations, accumulate

# 组合
list(combinations([1,2,3], 2))  # [(1,2), (1,3), (2,3)]

# 排列
list(permutations([1,2,3], 2))  # [(1,2), (1,3), (2,1), ...]

# 前缀和
list(accumulate([1,2,3,4]))  # [1, 3, 6, 10]
```

---

## 🔥 常用代码片段

```python
# 1. 二维数组初始化
dp = [[0] * n for _ in range(m)]  # ✅
dp = [[0] * n] * m                # ❌ 浅拷贝

# 2. 无穷大
INF = float('inf')
-INF = float('-inf')

# 3. 字符与ASCII互转
ord('a')  # 97
chr(97)   # 'a'

# 4. 字符串反转
s[::-1]

# 5. 列表去重
list(set(nums))

# 6. 字典按值排序
sorted(d.items(), key=lambda x: x[1])

# 7. 多变量赋值
a, b = b, a  # 交换

# 8. 判断奇偶
is_odd = (n & 1) == 1
```

---

## 🔗 相关文件

- 📊 [所有思维导图](../mindmaps/)
- 📖 [所有知识点](../knowledge/)
- 📋 [必刷题目清单](../practice/必刷题目清单.md)

**🎯 背会这些模板,刷题如虎添翼！**
