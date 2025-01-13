"""
左子树 < 根节点 < 右子树”

"""
from en.codes.python.chapter_array_and_linkedlist.linked_list import remove


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
    pre: 记录上一次的位置
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


def compute_degree(root: TreeNode) -> int:
    if not root:
        return 0
    degree = 0
    if root.left:
        degree += 1
    if root.right:
        degree += 1
    return degree


def delete(root: TreeNode, value: int) -> TreeNode:
    """
    节点数量，分 0、1 和 2 三种情况

    当待删除节点的度为0时，将待删除节直接删除.
    当待删除节点的度为1时，将待删除节点替换为其子节点即可。
    当待删除节点的度为2时，
        而需要使用一个节点替换该节点.

    """
    if not root:
        return None
    cur = root
    # 1.find
    pre = None
    child = 0
    while cur:
        if cur.value == value:
            break
        elif cur.value < value:
            pre = cur
            cur = cur.left
        elif cur.value > value:
            pre = cur
            cur = cur.right
    # 2.degree
    degree = compute_degree(cur)
    if degree == 0:
        # pre 是cur的父节点
        # cur 是叶子节点. pre.left = cur
        # 直接删除
        pre.left = None
        return

    if degree == 1:
        # pre 是cur的父节点
        # cur 是叶子节点. pre.left = cur
        # cur.left 只有左孩子
        # 将待删除节点替换为其子节点即可
        cur = cur.left
        return

    if degree == 2:
        # 1.找到待删除节点在“中序遍历序列”中的下一个节点，记为 tmp
        # 2.用tmp的值覆盖待删除节点的值，并在树中递归删除节点 tmp
        tmp: TreeNode = cur.right
        while tmp.left:
            tmp = tmp.left
        remove(tmp.value)
        cur.value = tmp.value
    return




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