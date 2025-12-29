from typing import List
"""
18. 四数之和
已解答
中等
相关标签
premium lock icon
相关企业
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution:
    def twoSumItem(self, nums: List[int], target: int, *arg: int) -> List[int]:
        """
        nums: 已经排序
        l, r
        """
        item_list = set()
        l, r = 0, len(nums) -1
        while l < r:
            s = nums[l] + nums[r]
            print(f"l: {l}, r: {r}, s: {s}")
            if s == target:
                item = (*arg, nums[l], nums[r])
                item_list.add(item)
                l += 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return list(item_list)

    def newArr(self, nums: List[int], i):
        return nums[i+1:]

    def threeSumItem(self, nums: List[int], target_val: int, cur_val: int) -> List[List[int]]:
        """
        上层已经排序
        """
        if len(nums) < 3:
            return []
        ret_list = list()
        cur = nums[0]
        n = len(nums)
        vist = set()
        for i in range(0, n):
            cur = nums[i]
            if cur in vist:
                continue
            vist.add(nums[i])
            tow_sum_val = target_val - cur
            arr = self.newArr(nums, i)
            item_list = self.twoSumItem(arr, tow_sum_val, cur_val, cur)
            print(f"i: {i}, cur:{cur}, twoSumItem sum {tow_sum_val}, arr:{arr} item_list:{item_list}")
            if item_list:
                ret_list.extend(item_list)
        return ret_list
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums = sorted(nums)
        ret_list = list()
        cur = nums[0]
        n = len(nums)
        vist = set()
        for i in range(0, n):
            #   跳过重复元素
            if nums[i] in vist:
                continue
            vist.add(nums[i])
            cur = nums[i]
            sum_val = target - cur
            arr = self.newArr(nums, i)
            item_list = self.threeSumItem(arr, sum_val, cur)
            print(f"i: {i}, cur:{cur}, threeSumItem sum {0-cur}, arr:{arr} item_list:{item_list}")
            if item_list:
                ret_list.extend(item_list)
        return ret_list



def main():
    """
 
    """
    # nums = [1,0,-1,0,-2,2]
    # target = 0
    # print(Solution().fourSum(nums, target))
    # nums = [2,2,2,2,2]
    # target = 8
    # print(Solution().fourSum(nums, target))
    nums = [0, 0, 0, 0]
    target = 0
    print(Solution().fourSum(nums, target))




if __name__ == '__main__':
    main()