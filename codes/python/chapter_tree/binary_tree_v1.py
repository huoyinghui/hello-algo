
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
    pass


if __name__ == '__main__':
    main()