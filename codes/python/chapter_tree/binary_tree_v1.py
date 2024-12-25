"""
bfs:
    基于task列表
    基于队列顺序优化

dfs:
    act:0 中序
    act:1 前序
    act:2 后序

dfs_mul: 多叉树
"""
from typing import List, Optional


class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: TreeNode | None) -> list[int]:
    """
    层序遍历
    """
    if root is None:
        return []
    data = list()
    task_level_node = [root]
    while task_level_node:
        new_task_level_node = []
        for node in task_level_node:
            data.append(node.val)
            if node.left:
                new_task_level_node.append(node.left)
            if node.right:
                new_task_level_node.append(node.right)
        task_level_node = new_task_level_node
    return data


def bfs_v2(root: TreeNode | None) -> list[int]:
    """
    层序遍历 deque

    广度优先遍历通常借助“队列”来实现。队列遵循“先进先出”的规则，而广度优先遍历则遵循“逐层推进”的规则，两者背后的思想是一致的
    """
    if root is None:
        return []
    from collections import deque
    queue = deque([root])
    data = list()
    while queue:
        # 从左出，右边入
        node = queue.popleft()
        data.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return data


def dfs(root: TreeNode | None, act: int = 0) -> list[int]:
    if root is None:
        return []
    data = [root.val]
    left = dfs(root.left, act=act)
    right = dfs(root.right, act=act)
    match act:
        case 0:
            return left + data + right
        case 1:
            return data + left + right
        case 2:
            return left + right + data


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=problem-list-v2&envId=tree&
        """
        if not root:
            return []
        return dfs(root, 0)


def main():
    """
                0
            1       2
        3     4    5   6
    """
    data_list = [0, 1, 2, 3, 4, 5, 6]
    n5 = TreeNode(data_list[5])
    n6 = TreeNode(data_list[6])
    n3 = TreeNode(data_list[3])
    n4 = TreeNode(data_list[4])
    n1 = TreeNode(data_list[1], left=n3, right=n4)
    n2 = TreeNode(data_list[2], left=n5, right=n6)
    root = TreeNode(data_list[0], left=n1, right=n2)
    print(bfs(root))
    print(bfs_v2(root))

    # print(dfs(root, 0))
    print(dfs(root, 1))
    pass


if __name__ == '__main__':
    main()