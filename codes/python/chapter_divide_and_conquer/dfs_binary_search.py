from typing import List


def dfs_binary_search(arr: List[int] = None, target: int = 0, i: int = 0, j: int = 0):
    """
    dfs
    """
    if not arr:
        return -1
    mid = (i+j)//2
    if arr[mid] == target:
        # 找到了
        return mid

    if arr[mid] > target:
        # target [0, mid]
        return dfs_binary_search(arr=arr, target=target, i=i, j=mid-1)
    else:
        # target [i, mid]
        return dfs_binary_search(arr=arr, target=target, i=mid+1, j=j)


def main():
    target = 6
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]

    # 二分查找（双闭区间）
    index = dfs_binary_search(arr=nums, target=target, i=0, j=len(nums)-1)
    print("目标元素 6 的索引 = ", index)
    return


if __name__ == "__main__":
    main()