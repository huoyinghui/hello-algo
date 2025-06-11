from typing import List, reveal_type


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # 定义dp[i]: 在i位置获得最大收益
        dp = [0] * (len(nums) + 1)
        # 初始状态
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # yes / no
            yes = dp[i-2] + nums[i]
            no = dp[i-1]
            dp[i] = max(yes, no)
        # 迭代
        return dp[n-1]


def main():
    nums = [0]
    # nums = [1, 2, 3, 1]
    ret = Solution().rob(nums=nums)
    print(ret)
    pass


if __name__ == '__main__':
    main()

"""

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""