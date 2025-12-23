## 6. 常用代码片段 🔥

# 1. 二维数组初始化
m, n = 3, 4
dp = [[0] * n for _ in range(m)]  # ✅ 正确
# dp = [[0] * n] * m                # ❌ 浅拷贝，错误！
print(f"二维数组初始化 dp: {dp}")

# 2. 无穷大/无穷小
INF = float('inf')
NEG_INF = float('-inf')
print(f"无穷大/无穷小 INF: {INF}, NEG_INF: {NEG_INF}")

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
nums = [1, 4, 2, 2, 3, 4, 4, 5]
print(f"列表去重（不保持顺序）: {list(set(nums))}")
# 列表去重（不保持顺序）: [1, 2, 3, 4, 5]
print(f"列表去重（保持顺序）: {dedupe(nums)}")
# 列表去重（保持顺序）: [1, 4, 2, 3, 5]

# 6. 字典按值排序
d = {'a': 3, 'b': 1, 'c': 2}
# sorted(d.items(), key=lambda x: x[1])  # [('b', 1), ('c', 2), ('a', 3)]
print(f"字典按值排序: {sorted(d.items(), key=lambda x: x[1])}")
# 字典按值排序: [('b', 1), ('c', 2), ('a', 3)]


# 7. 多变量赋值
a, b = 1, 2
a, b = b, a  # 交换
a, b, c = 1, 2, 3

# 8. 判断奇偶
n = 7
is_odd = (n & 1) == 1
print(f"判断奇偶 is_odd: {is_odd}") # True
is_even = (n & 1) == 0
print(f"判断奇偶 is_even: {is_even}") # False


# 9. 整数除法（向下取整）
print(f"整数除法（向下取整） 7 // 2: {7 // 2}")  # 3
print(f"整数除法（向下取整） -7 // 2: {-7 // 2}")  # -4

# 10. 进制转换
print(f"进制转换 bin(10): {bin(10)}")  # '0b1010' 二进制
print(f"进制转换 oct(10): {oct(10)}")  # '0o12' 八进制
print(f"进制转换 hex(10): {hex(10)}")  # '0xa' 十六进制

# 11. 列表推导式
squares = [x**2 for x in range(10)]
print(f"列表推导式 squares: {squares}")
# 列表推导式 squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(10) if x % 2 == 0]
print(f"列表推导式 evens: {evens}")
# 列表推导式 evens: [0, 2, 4, 6, 8]
matrix = [[0] * n for _ in range(m)]
print(f"列表推导式 matrix: {matrix}")
# 列表推导式 matrix: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 12. 字典推导式
items = [('a', 1), ('b', 2), ('c', 3)]
new_dict =  {k: v for k, v in items if v > 1}
print(f"字典推导式 new_dict: {new_dict}")
new_dict_2 = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(f"字典推导式 new_dict_2: {new_dict_2}")


# 13. 集合推导式
new_set = {x for x in nums if x > 0}
print(f"集合推导式 new_set: {new_set}")


# 14. 生成器表达式
gen = (x**2 for x in range(10))  # 节省内存
print(f"生成器表达式 gen: {gen}")
