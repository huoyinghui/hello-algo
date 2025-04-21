
def solve(n: int = 0, choice: list[int] = None) -> int:
    """
    dp[n] = []
    """
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    # 1: dp[2] + 1
    # 2: dp[1] + 1
    dp[3] = max(dp[2]+1, dp[1]+1)
    return 0


def main():
    """
    给定一个共有 n 阶的楼梯，你每步可以上 1 阶或者2 阶，请问有多少种方案可以爬到楼顶？
    """
    ret = solve(1, choice=[1, 2])
    print(ret)
    pass


if __name__ == '__main__':
    main()