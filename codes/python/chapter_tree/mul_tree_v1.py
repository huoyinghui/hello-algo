from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


def dfs_mul_postorder(root=None, act: int = 0) -> list[int]:
    """
    https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
    """
    if not root:
        return []
    data = [root.val]
    item_list = []
    if not root.children:
        return data
    for child in root.children:
        item = dfs_mul_postorder(child, act=act)
        item_list.extend(item)
    match act:
        case 0:
            return item_list + data
        case 1:
            return data + item_list
        case _:
            return data + item_list


def main():
    """
                1
            3   2  4
         5   6 7
    """
    root = Node(
        val=1,
        children=[
            Node(val=3, children=[
                Node(val=5),
                Node(val=6),
                Node(val=7),
            ]),
            Node(val=2),
            Node(val=4),
        ],
    )
    print(dfs_mul_postorder(root, act=0))
    print(dfs_mul_postorder(root, act=1))
    pass


if __name__ == '__main__':
    main()