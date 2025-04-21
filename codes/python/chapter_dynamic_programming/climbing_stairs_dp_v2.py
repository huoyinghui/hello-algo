from itertools import count
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


def main():
    n = 6
    c = Solution().climbStairs(n=n)
    print(c)
    pass


if __name__ == '__main__':
    main()