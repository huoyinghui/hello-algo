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
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 1:
            return nums[0]
            
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, n):
            dp[i+1] = max(dp[i], dp[i-1]+nums[i])
        return dp[n]



def main():
    # nums = [2,7,9,3,1]
    nums = [1,2,3,1]
    ret = Solution().rob(nums)
    print(ret)


    pass

if __name__ == '__main__':
    main()
