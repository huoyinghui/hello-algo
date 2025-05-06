from itertools import count
from math import inf
from typing import List
from functools import lru_cache


class Solution:
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？



示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
    """

    @classmethod
    @lru_cache()
    def dfs(cls, i: int = 0):
        """
        dfs
        """
        # 1: 1
        # 2: 2
        # dp[3] = dp[2] + dp[1] = 3
        # dp[4] = dp[3] + dp[2] = 5
        #  1       2      3      5     8     13
        # dp[1], dp[2], dp[3], dp[4], dp[5], dp[6].... dp[i]
        if i < 3:
            return i
        return cls.dfs(i=i-1) + cls.dfs(i=i-2)

    def climb_stairs_dp(self, n: int) -> int:
        """
        经典 DP 模板是：
            1.	状态定义：dp[i] / dp[i][j] 是什么含义？代表什么子问题？
            2.	转移方程：从哪些状态转移到当前状态？
            3.	初始化：边界情况如何设置？
            4.	遍历顺序：从前往后 or 递归记忆化？
            5.	返回值：最终要求解的状态是哪个？

        """
        # 1.dp[i]表示爬到第i个位置的方案数
        dp = [0] * (n+1)
        # 3.初始化
        dp[1] = 1
        dp[2] = 2
        # 4.遍历 3-n
        for i in range(3, n+1):
            # 2 转移方程:
            dp[i] = 0
        # 5.返回结果
        return dp[n]


def main():
    # prices = [7, 6, 4, 3, 1]
    n = 3
    ret = Solution().climb_stairs_dp(n=n)
    print(ret)


if __name__ == '__main__':
    main()
