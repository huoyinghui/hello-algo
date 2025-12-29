### 2.3 deque - 双端队列
# **应用场景：**
# - BFS队列
# - 滑动窗口
# - 循环缓冲

from collections import deque

# 创建
dq = deque([1, 2, 3])

# 右端操作 
dq.append(4)        # [1, 2, 3, 4]
dq.pop()            # 4, [1, 2, 3]

# 左端操作 
dq.appendleft(0)    # [0, 1, 2, 3]
print(f"dq.appendleft: {dq}")
dq.popleft()        # 0, [1, 2, 3]
print(f"dq.popleft: {dq}")

# 旋转 
dq.rotate(1)        # [3, 1, 2] 向右旋转
print(f"dq.rotate: {dq}")
dq.rotate(-1)       # [1, 2, 3] 向左旋转
print(f"dq.rotate(-1): {dq}")

# 限制长度
dq = deque(maxlen=3)
dq.extend([1, 2, 3, 4])  # deque([2, 3, 4], maxlen=3)
print(f"dq: {dq}")
