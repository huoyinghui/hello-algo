### 1.2 enumerate, sorted, reversed

# enumerate - 同时获取索引和值
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c

# enumerate指定起始索引
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(i, val)  # 1 a, 2 b, 3 c

# sorted - 排序（返回新列表）
print(sorted([3, 1, 4, 1, 5]))  # [1, 1, 3, 4, 5]
print(sorted([3, 1, 4], reverse=True))  # [4, 3, 1]
print(sorted(['apple', 'pie', 'a'], key=len))  # ['a', 'pie', 'apple']

# 多关键字排序
points = [(1, 2), (3, 1), (1, 1)]
print(sorted(points, key=lambda x: (x[0], x[1])))

# reversed - 反转迭代器
print(list(reversed([1, 2, 3])))  # [3, 2, 1]