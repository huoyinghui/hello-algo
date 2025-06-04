class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        # dp = [-1] * (n+1)
        # dp[0] = 0
        b = 0
        # a dp[i-1]
        # dp[1] = 1
        a = 1
        for i in range(2, n+1):
            # n
            # dp[i] = dp[i-1] + dp[i-2]
            n = a + b
            b = a
            a = n
        return a


def main():
    n = 3
    ret = Solution().fib(n)
    print(ret)


if __name__ == '__main__':
    main()