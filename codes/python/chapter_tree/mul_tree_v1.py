from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


def dfs_mul_postorder(root: Node | None) -> list[int]:
    """
    https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/
    """
    if root is None:
        return []
    data = [root.val]
    item_list = []
    for child in root.children:
        item = dfs_mul_postorder(child)
        item_list.extend(item)
    return item_list + data


def main():
    pass

if __name__ == '__main__':
    main()