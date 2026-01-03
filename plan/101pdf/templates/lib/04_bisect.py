
## 4. bisect 模块 - 二分查找 🐍

from ast import main
import bisect
from operator import le

nums = [1, 3, 5, 7, 9]

# bisect_left - 查找插入位置（左边界）
pos = bisect.bisect_left(nums, 5)   # 2
print(f"bisect_left(5): {pos}")
pos = bisect.bisect_left(nums, 6)   # 3
print(f"bisect_left(6): {pos}")

# bisect_right - 查找插入位置（右边界）
pos = bisect.bisect_right(nums, 5)  # 3
print(f"bisect_right(5): {pos}")
pos = bisect.bisect(nums, 5)        # 同bisect_right, 3
print(f"bisect.bisect(5): {pos}")

# insort - 插入并保持有序
bisect.insort(nums, 4)  # [1, 3, 4, 5, 7, 9]
print(f"insort(4): {nums}")
bisect.insort_left(nums, 5)
print(f"insort_left(5): {nums}")
bisect.insort_right(nums, 5)
print(f"insort_right(5): {nums}")

# 应用：查找区间
def count_range(nums, left, right):
    """统计[left, right]范围内的元素个数"""
    l = bisect.bisect_left(nums, left)
    r = bisect.bisect_right(nums, right)
    return r - l
# nums:[1, 3, 4, 5, 5, 5, 7, 9],count_range(3, 7): 6
print(f"nums:{nums},count_range(3, 7): {count_range(nums, 3, 7)}")






def bisect_search(nums: list[int], target: int):
    left, right = 0, len(nums) -1

    # [0, n-1]
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # [left, mid-1]
            right = mid - 1
    return mid


def bisect_search_left(nums: list[int], target: int):
    left, right = 0, len(nums) -1

    # [0, n-1]
    while left <= right:
        mid = left + (right-left) // 2
        print(f"left: {left}, right: {right}, mid: {mid}")
        if nums[mid] == target:
            print(f"find target: {target} ")
            # [left, mid-1]
            right = mid-1
        elif nums[mid] < target:
            # [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # [left, mid-1]
            right = mid - 1
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

def bisect_search_right(nums: list[int], target: int):
    left, right = 0, len(nums) -1

    # [0, n-1]
    while left <= right:
        mid = left + (right-left) // 2
        print(f"left: {left}, right: {right}, mid: {mid}")
        if nums[mid] == target:
            print(f"find target: {target} ")
            # [left, mid-1]
            left = mid + 1
        elif nums[mid] < target:
            # [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # [left, mid-1]
            right = mid - 1
    if right < 0 or nums[right] != target:
        return -1
    return right

def main():
    """测试用例"""
    nums = [1, 2, 3, 4, 5]
    target = 3
    ret = bisect_search(nums, target)
    print(f"main {ret}")
    nums = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    # ret = bisect_search_left(nums, target)
    ret = bisect_search_right(nums, target)
    print(f"main bisect_search_right {ret}")
    pass

if __name__ == "__main__":
    main()
