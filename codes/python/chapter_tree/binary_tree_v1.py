
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
    pass


if __name__ == '__main__':
    main()