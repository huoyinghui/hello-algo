### 2.1 Counter - 计数器

from collections import Counter

# 统计频率
nums = [1, 1, 2, 3, 3, 3]
counter = Counter(nums)
print(counter)
# Counter({3: 3, 1: 2, 2: 1})

# 最常见的k个元素
print( counter.most_common(2) )  # [(3, 3), (1, 2)]

# 字符串统计
s = "hello world"
char_count = Counter(s)
print(char_count)
# Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Counter运算
c1 = Counter(['a', 'b', 'c'])
c2 = Counter(['a', 'b', 'd'])
print("c1+c2", c1 + c2)  # 相加 Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
print("c1-c2", c1 - c2)  # 相减 Counter({'c': 1})
print("c1&c2", c1 & c2)  # 交集 Counter({'a': 1, 'b': 1})
print("c1|c2", c1 | c2)  # 并集 Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})

# 实用技巧
print(counter['x'])  # 不存在返回0，不报错
