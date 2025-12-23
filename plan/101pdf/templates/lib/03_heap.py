
## 3. heapq 模块 - 堆 🐍

# **典型应用：**
# - LeetCode 215. 数组中的第K个最大元素
# - LeetCode 23. 合并K个升序链表
# - LeetCode 347. 前K个高频元素

import heapq

# 小顶堆
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(f"heap: {heap}")
min_val = heapq.heappop(heap)  # 1
print(f"min_val: {min_val}")

# 批量建堆
nums = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(nums)  # O(n) 原地建堆
print(f"批量建堆 nums: {nums}")

# Top K问题
# heapq.nlargest(3, nums)    # [9, 6, 5]
print(f"nlargest: {heapq.nlargest(3, nums)}")
# heapq.nsmallest(3, nums)   # [1, 1, 2]
print(f"nsmallest: {heapq.nsmallest(3, nums)}")

# 大顶堆（使用负数）
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
print(f"大顶堆（使用负数） max_heap: {max_heap}")
max_val = -heapq.heappop(max_heap)  # 3
print(f"大顶堆（使用负数） max_val: {max_val}")

# 堆排序
def heap_sort(nums):
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]

# 合并有序序列
merged = heapq.merge([1, 3, 5], [2, 4, 6])
print(f"merged: {list(merged)}")
# [1, 2, 3, 4, 5, 6]
