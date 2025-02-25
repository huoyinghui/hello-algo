from typing import List


def binary_search(arr: List[int] = None, target: int = None) -> int:
    """
    二分查找（双闭区间)
    return: the index of the target element in the array
    """
    if not arr:
        return -1
    # 初始化双闭区间 [0, n-1] ，即 i, j 分别指向数组首元素、尾元素
    i, j = 0, len(arr) - 1
    # 循环，当搜索区间为空时跳出（当 i > j 时为空）
    while i <= j:
        # 计算中点索引 m, 向下取整
        m = (i+j)//2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            # target 在区间 [m+1, j] 中
            i = m + 1
        elif arr[m] > target:
            # target 在区间 [i, m-1] 中
            j = m - 1
    return -1


def main():
    target = 6
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]

    # 二分查找（双闭区间）
    index = binary_search(nums, target)
    print("目标元素 6 的索引 = ", index)
    pass


if __name__ == '__main__':
    main()