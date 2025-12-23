## 5.oitertools 模块 🐍
"""
组合与排列的区别
    * 组合 C(n, k)：
        不考虑元素顺序，例如从 {1, 2, 3} 中选 2 个元素进行组合：(1,2), (1,3), (2,3)，共 3 种
    * 排列 A(n, k)：
        考虑元素顺序，例如从 {1, 2, 3} 中选 2 个元素进行排列：(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)，共 6 种
    关系：A(n, k) = C(n, k) × k!，即排列数等于组合数乘以 k 个元素的全排列数。



笛卡尔积: 
    * 笛卡尔积：两个集合的笛卡尔积是所有可能的有序对的集合，
        例如 {1, 2} 和 {'a', 'b'} 的笛卡尔积是 {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}。
    * 如果集合 A 有 m 个元素，集合 B 有 n 个元素，则 A × B 有 m × n 个元素。
    * 可以扩展到多个集合：A × B × C 包含所有可能的三元组 (a, b, c)，其中 a ∈ A, b ∈ B, c ∈ C。
"""


from itertools import combinations, permutations, product, accumulate, chain, islice, groupby

# combinations - 组合 C(n, k)
print(f"组合 C(n, k) {list(combinations([1, 2, 3], 2))}")
# [(1, 2), (1, 3), (2, 3)]

# permutations - 排列 A(n, k)
# list(permutations([1, 2, 3], 2))
print(f"排列 A(n, k) {list(permutations([1, 2, 3], 2))}")
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# product - 笛卡尔积
# list(product([1, 2], ['a', 'b']))
print(f"笛卡尔积 {list(product([1, 2], ['a', 'b']))}")
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# accumulate - 累积（前缀和）
#  f(x) = f(x-1) + x
print(f"累积（前缀和） {list(accumulate([1, 2, 3, 4]))}")  # [1, 3, 6, 10]
#  f(x) = f(x-1) * x
print(f"累积（前缀和） {list(accumulate([1, 2, 3, 4], lambda x, y: x * y))}")  # [1, 2, 6, 24]

# chain - 连接多个迭代器
print(f"连接多个迭代器 {list(chain([1, 2], [3, 4]))}")  # [1, 2, 3, 4]

# islice - 切片迭代j
# 普通列表切片 lst[start:end] 直接返回一个新列表
list(islice([1, 2, 3, 4, 5], 2, 4))  # [3, 4]
print(f"切片迭代器 {list(islice([1, 2, 3, 4, 5], 2, 4))}")  # [3, 4]

# groupby - 分组
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))