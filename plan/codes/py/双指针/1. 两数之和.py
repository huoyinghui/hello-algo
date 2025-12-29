from typing import List
"""
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     """
    #     l, r
    #     """
    #     l, r = 0, len(nums) -1
    #     nums = sorted(nums)
    #     while l < r:
    #         s = nums[l] + nums[r]
    #         if s == target:
    #             return [nums[l], nums[r]]
    #         elif s < target:
    #             l += 1
    #         else:
    #             r -= 1
    #     return []
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        dict = {}
        O(n)
        """
        ret = {}
        for i, num in enumerate(nums):
            other = target - num 
            if other in ret:
                return [ret[other], i]
            else:
                ret[num] = i
        return []
    


def main():
    nums = [2,7,11,15]
    target = 9
    ret = Solution().twoSum(nums, target)
    print(ret)
    pass


if __name__ == '__main__':
    main()
