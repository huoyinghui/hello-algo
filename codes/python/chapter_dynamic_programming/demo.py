from functools import lru_cache
from random import choice


def backtrack(choices: list[int], state: int, n: int, res: list[int]) -> int:
    """
    1.状态
    2.做选择
    3.回退
    """
    # 超过了，不需要更新，回退
    if state > n:
        return res[0]

    # 当爬到第 n 阶时，方案数量加 1
    if state == n:
        res[0] += 1
        return res[0]

    # 遍历所有选择: 还没有到，继续选择
    for choice in choices:
        # 剪枝：不允许越过第 n 阶
        select_state = state + choice
        if select_state > n:
            # 不执行, 放弃本次选择
            continue
        # 尝试：做出选择，更新状态
        backtrack(choices=choices, state=select_state, n=n, res=res)
        # 回退
    return res[0]


def climbing_stairs_backtrack(n: int) -> int:
    """
    爬楼梯：回溯
    """
    # 可选择向上爬 1 阶或 2 阶
    choices = [1, 2]
    # 从第 0 阶开始爬
    state = 0
    # 使用 res[0] 记录方案数量
    res = [0]
    backtrack(choices=choices, state=state, n=n, res=res)
    return res[0]


def solve(n: int = 0, choice: list[int] = None) -> int:
    """
    dp[n] = []
    """
    dp = [0] * (n+1)
    dp[0] = 0
    if n <= 2:
        return n
    dp[1] = 1
    dp[2] = 2
    # 1: dp[2] + 1
    # 2: dp[1] + 1
    # dp[3] = max(dp[2]+1, dp[1]+1)
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


@lru_cache(maxsize=None)
def dfs(i: int = 0):
    """
    暴力搜索
    设爬到第i阶共有dp[i]种方案，那么就是原问题，其子问题包括：dp[i-1], ...dp[2], dp[1]

    由于每轮只能上1阶或2阶，因此当我们站在第i阶楼梯上时, 上一轮只可能站在第i-1阶或第i-2阶上

    由此便可得出一个重要推论：
        第i阶的方案数: 爬到第 i-1 阶的方案数加上爬到第 i-2 阶的方案数就等于爬到
    dp[i] = dp[i-1] + dp[i-2]
    """
    # 已知 dp[1] 和 dp[2] ，返回之
    if i == 1 or i == 2:
        return i
    count = dfs(i-1) + dfs(i-2)
    return count


def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯：搜索"""
    return dfs(n)


def main():
    """
    给定一个共有 n 阶的楼梯，你每步可以上 1 阶或者2 阶，请问有多少种方案可以爬到楼顶？
    """
    ret = solve(38, choice=[1, 2])
    # 63245986
    # ret = climbing_stairs_dfs(n=38)
    # ret = climbing_stairs_backtrack(n=38)
    print(ret)
    pass


if __name__ == '__main__':
    main()