
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def search(root: TreeNode = None, value: int = None) -> TreeNode | None:
    if not root:
        return None
    cur = root
    while cur:
        if value < cur.value:
            cur = cur.left
        elif value > cur.value:
            cur = cur.right
        else:
            # 找到
            return cur
    # 循环结束，没有找到
    return None


def insert(root: TreeNode, value: int) -> TreeNode:
    """
    插入节点
    1.查找插入位置
    2.在该位置插入节点
    """
    if not root:
        return None

    cur = root
    pre = None
    while cur:
        if cur.value == value:
            # 已经存在
            return None
        elif cur.value < value:
            # 去右子树
            pre = cur
            cur = cur.right
        elif cur.value > value:
            # 去左子树
            pre = cur
            cur = cur.left

    # target
    target = TreeNode(value)
    if target.value > pre.value:
        pre.right = target
    else:
        pre.left = target
    return target


def main():
    """
                4
            2       6
        1     3    5
    """
    data_list = [4, 2, 6, 1, 3, 5]
    root = TreeNode(data_list[0])
    for value in data_list[1:]:
        insert(root, value)
    # n5 = TreeNode(data_list[5])
    #
    # n3 = TreeNode(data_list[3])
    # n4 = TreeNode(data_list[4])
    #
    # n1 = TreeNode(data_list[1], left=n3, right=n4)
    # n2 = TreeNode(data_list[2], left=n5)
    #
    # root = TreeNode(data_list[0], left=n1, right=n2)
    node = search(root, 3)
    print(node, node.value if node else None)
    pass


if __name__ == '__main__':
    main()