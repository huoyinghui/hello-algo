from ast import main
from gettext import find
from operator import le
from typing import List

def merge(left, right):
    ret = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
    if i < len(left):
        ret.extend(left[i:])
    if j < len(right):
        ret.extend(right[j:])
    return ret

def merge_sort(num: List[int] = None):
    n = len(num)
    if n <= 1:
        return num
    mid = len(num) // 2 
    left = merge_sort(num[:mid])
    right = merge_sort(num[mid:])
    return merge(left, right)

# select
# for
# 1.find_min
# 2.swap

def swap(num, i, j):
    num[i], num[j] = num[j], num[i]
    return num

def find_min(num, i):
    ret_min = 0
    for j in range(i, len(num)):
        ret_min = min(ret_min, num[j])
    return ret_min


def find_min_idx(num, i):
    ret_min_idx = i
    for j in range(i+1, len(num)):
        if num[j] < num[ret_min_idx]:
            ret_min_idx = j
    return ret_min_idx

def select_sort(nums):
    for i in range(len(nums)):
        min_idx = find_min_idx(nums, i)
        if min_idx:
            swap(nums, i, min_idx)
    return nums



def main():
    num = [3, 1, 4, 1, 5, 9, 2, 6]
    # ret  = merge_sort(num)
    ret = select_sort(num)
    print(ret)
    return num

main()