from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        dict = {}
        O(n)
        """
        ret = {}
        item_list = set()
        for i, num in enumerate(nums):
            other = target - num 
            if other in ret:
                # item = [ret[other], i]
                # item_list.append(item)
                item = (other, num)
                item_list.add(item)
            else:
                ret[num] = i
        return list(item_list)

    def newArr(self, nums: List[int], i):
        # if i <= 0:
        #     return nums[1:]
        # arr = nums[0:i] + nums[i+1:]
        # return arr
        return nums[i+1:]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
        注意：答案中不可以包含重复的三元组。
        """
        if len(nums) < 3:
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
            arr = self.newArr(nums, i)
            ret = self.twoSum(arr, 0-cur)
            # print(f"i: {i}, cur:{cur}, tow sum {0-cur}, arr:{arr} ret:{ret}")
            if ret:
                item = [(nums[i], *v) for v in ret]
                ret_list.extend(item)
        # return list(ret_list)
        return ret_list


def main():
    """
    https://leetcode.cn/problems/1fGaJU/submissions/687980583/
    示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
    """
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0]
    nums = [0, 0, 0, 0]
    print(Solution().threeSum(nums))


if __name__ == '__main__':
    main()