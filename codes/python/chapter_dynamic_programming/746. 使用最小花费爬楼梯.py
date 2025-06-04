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
        起点：可以是第 0 或第 1 阶
        •	每次跳之前，要先付当前阶的费用
        •	每次可以跳 1 或 2 阶
        •	目标是到达「楼梯之外的下一阶」，不用付最后一步的代价
        """
        if not cost:
            return 0
        # 1.定义dp
        n = len(cost)
        dp = [0] * (n+1)
        dp[0] = 0  # 起点可以是 cost[0]，不付费
        # dp[1] = min(0, cost[1])  # 或者 cost[1]，也不付费
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]


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
    cost = [10, 15, 20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    ret = Solution().minCostClimbingStairs(cost=cost)
    print(ret)


if __name__ == '__main__':
    main()
