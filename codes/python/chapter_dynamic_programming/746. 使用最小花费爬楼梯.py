from itertools import count
from math import inf
from typing import List
from functools import lru_cache


class Solution:
    """
    746. 使用最小花费爬楼梯
简单
相关标签
相关企业
提示
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。


    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp[i]: 到达第i个台阶的最小话费
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        """
        if not cost:
            return 0
        n = len(cost)
        dp = [inf] * n
        dp[0] = cost[0]
        for i in range(1, n):
            dp[i] = 0
        return 0


def main():
    """
    示例 1：

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。
示例 2：

输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
    """
    # prices = [7, 6, 4, 3, 1]
    cost = [10, 15, 20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ret = Solution().minCostClimbingStairs(cost=cost)
    print(ret)


if __name__ == '__main__':
    main()
