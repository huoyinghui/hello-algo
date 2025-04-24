from itertools import count
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
        grid = [
            [1, 3, 1], [1, 5, 1], [4, 2, 1]
        ]
        dp[
          []
        ]
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


def main():
    # n = 6
    # c = Solution().climbStairs(n=n)
    # print(c)
    # grid = [[1, 2, 3], [4, 5, 6]]
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    c = Solution().minPathSum(grid=grid)
    print(c)
    pass


if __name__ == '__main__':
    main()