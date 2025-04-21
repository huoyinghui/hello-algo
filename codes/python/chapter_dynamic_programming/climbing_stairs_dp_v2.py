from itertools import count

class Solution:

    @classmethod
    def dfs(cls, i: int = 0):
        """

        """
        # 1: 1
        # 2: 2
        # dp[3] = dp[2] + dp[1] = 3
        # dp[4] = dp[3] + dp[2] = 5
        #  1       2      3      5     8
        # dp[1], dp[2], dp[3], dp[4], dp[5], dp[6].... dp[i]
        if i < 3:
            return i
        count = cls.dfs(i-1) + cls.dfs(i-2)
        return count

    def climbStairs(self, n: int) -> int:
        return self.dfs(n)
