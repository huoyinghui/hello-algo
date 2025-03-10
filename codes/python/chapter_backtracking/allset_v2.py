from pipes import stepkinds
from typing import List


def backtrack(
    state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]
):
    """回溯算法：全排列 I"""
    # 当状态长度等于元素数量时，记录解
    if len(state) == len(choices):
        res.append(list(state))
        return
    # 遍历所有选择
    for i, choice in enumerate(choices):
        # 剪枝：不允许重复选择元素
        if not selected[i]:
            # 尝试：做出选择，更新状态
            selected[i] = True
            state.append(choice)
            # 进行下一轮选择
            backtrack(state, choices, selected, res)
            # 回退：撤销选择，恢复到之前的状态
            selected[i] = False
            state.pop()


def backtrack2(choices: list[int], state: List[int] = None, selected: list[bool] = None, res: list[list[int]] = None):
    """
    1.遍历
    2.选择
    3.下一轮状态
    4.回退
    """
    # 终止
    if len(state) == len(choices):
        res.append(list(state))
        return

    for idx, choice in enumerate(choices):
        if selected[idx]:
            continue
        # 选择
        selected[idx] = True
        state.append(choice)

        # 下一轮:
        # choice:
        backtrack2(choices=choices, state=state, selected=selected, res=res)

        # 回退: 撤销选择,
        selected[idx] = False
        state.pop()
    return


def permutations_i(nums: list[int]) -> list[list[int]]:
    """
    res: 最终的结果保存
    selected: 剪枝
    nums: 选择
    """
    res = []
    selected = [False] * len(nums)
    backtrack2(state=[], choices=nums, selected=selected, res=res)
    return res


"""Driver Code"""
if __name__ == "__main__":
    nums = [1, 2, 3]

    res = permutations_i(nums)

    print(f"输入数组 nums = {nums}")
    print(f"所有排列 res = {res}")
