### 1.3 all, any, sum, max, min

# all - 全部为True
print(all([True, True, False]))  # False
print(all([1, 2, 3]))  # True
print(all([]))  # True (空列表)

# any - 任一为True
print(any([False, False, True]))  # True
print(any([0, 0, 1]))  # True
print(any([]))  # False

# sum - 求和
print(sum([1, 2, 3, 4]))      # 10
print(sum([1, 2, 3], 10))  # 16 (起始值10)

# max, min - 最大最小值
print(max([1, 5, 3]))  # 5
print(min([1, 5, 3]))  # 1
print(max('abc'))  # 'c'
print(max([1, 2, 3], key=lambda x: -x))  # 1
