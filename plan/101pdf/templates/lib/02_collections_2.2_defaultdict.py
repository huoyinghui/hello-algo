### 2.2 defaultdict - 默认字典

from collections import defaultdict

# 默认值为int
count = defaultdict(int)
for num in [1, 2, 1, 3]:
    count[num] += 1  # 不用检查键是否存在
print(f"count: {count}")
# defaultdict(<class 'int'>, {1: 2, 2: 1, 3: 1})

# 默认值为list
graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)
print(f"graph: {graph}")
# defaultdict(<class 'list'>, {1: [2, 3]})

# 默认值为set
groups = defaultdict(set)
groups['A'].add(1)
groups['A'].add(2)
# defaultdict(<class 'set'>, {'A': {1, 2}})
print(f"groups: {groups}")
# 自定义默认值
d = defaultdict(lambda: 'N/A')
# d: defaultdict(<function <lambda> at 0x1030dc220>, {'key': 'N/A'})
d['key']  # 'N/A'
print(f"d: {d}")
