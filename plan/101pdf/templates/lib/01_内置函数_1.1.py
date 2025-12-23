### 1.1 map, filter, zip
# map - 映射
squares = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(squares)
# [1, 4, 9, 16]

# filter - 过滤
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(evens)
# [2, 4]

# zip - 并行迭代
pairs = list(zip([1, 2, 3], ['a', 'b', 'c']))
print(pairs)
# [(1, 'a'), (2, 'b'), (3, 'c')]

# zip解包
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for a, b in zip(nums1, nums2):
    print(a, b)


