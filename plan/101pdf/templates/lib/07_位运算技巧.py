## 7. Python位运算技巧

# 判断奇偶
n = 7
n & 1 == 1  # 奇数
print(f"判断奇偶: {n & 1 == 1}")

# 乘以/除以2的幂
n << 1  # n * 2
print(f"乘以/除以2的幂: {n << 1}")
n >> 1  # n // 2
print(f"乘以/除以2的幂: {n >> 1}")


# 交换两个数
a, b = 1, 2
print(f"交换两个数{a, b}")
a ^= b # a = a ^ b
print(f"step1: a ^=b: {a}, b: {b}")
b ^= a # b = b ^ a = b ^ a ^ b = a
print(f"step2: b ^=a: {a}, b: {b}") # 完成b->a
a ^= b # a = a ^ b = a ^ a ^ b = b
print(f"step3: b ^=a: {a}, b: {b}") # 完成b->a

# 判断是否为2的幂
n > 0 and (n & (n - 1)) == 0
print(f"判断是否为2的幂: {n > 0 and (n & (n - 1)) == 0}")


# 获取最低位的1
n & -n

# 去掉最低位的1
n & (n - 1)

# 统计1的个数
# bin(n).count('1')
print(f"统计1的个数: {bin(n).count('1')}")