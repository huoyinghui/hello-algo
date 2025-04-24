from itertools import count
from math import inf
from typing import List
from functools import lru_cache


class Solution:

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

    def climbStairs(self, n: int) -> int:
        return self.dfs(n)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass

    def minCostPath(self, cost: List[List[int]] = None):
        """
        给定一个 m * n 的二维网格 grid ，
        网格中的每个单元格包含一个非负整数，表示该单元格的代价。
        机器人以左上角单元格为起始点，每次只能向下或者向右移动一步，直至到达右下角单元格。请返回从左上角到右下角的最小路径和。

        """
        return

    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.cn/problems/0i0mDW/description/
        给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
        说明：一个机器人每次只能向下或者向右移动一步。
        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]

        最优子结构: 关联的状态
            对于状态[j, i]，它只能从上边格子[j-1][i] 和左边格子[j][i-1]转移而来.
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]

        #step1: 初始状态
        dp[0][0] = grid[0][0]
        # 第一行: dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        # 第一列: dp[j][0] = dp[j-1] + grid[j][0]
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]

        # step2: 迭代
        for j in range(1, m):
            for i in range(1, n):
                # 相邻的前两个
                dp[j][i] = min(dp[j][i-1], dp[j-1][i]) + grid[j][i]
        return dp[m-1][n-1]

    def minPathSum_dfs(self, has=None, grid=None, i=0, j=0) -> int:
        """
        最小路径和：暴力搜索
        i: 行
        j: 列

        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        """
        # 若行列索引越界，则返回 +∞ 代价
        if i < 0 or j < 0:
            return inf
        if i == 0 and j == 0:
            return grid[0][0]
        key = f"{i}_{j}"
        if key in has:
            return has[key]
        up = self.minPathSum_dfs(has=has, grid=grid, i=i-1, j=j)
        left = self.minPathSum_dfs(has=has, grid=grid, i=i, j=j-1)
        cost = min(up, left) + grid[i][j]
        has[f"{i}_{j}"] = cost
        return cost


def main():
    # n = 6
    # c = Solution().climbStairs(n=n)
    # print(c)
    grid = [[1, 2, 3], [4, 5, 6]]
    # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # c = Solution().minPathSum(grid=grid)
    has = {}
    c = Solution().minPathSum_dfs(has=has, grid=grid, i=len(grid)-1, j=len(grid[0])-1)
    print(c)
    pass


if __name__ == '__main__':
    main()