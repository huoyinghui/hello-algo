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
    # ret = solve(1, choice=[1, 2])
    # print(ret)
    pass


if __name__ == '__main__':
    main()