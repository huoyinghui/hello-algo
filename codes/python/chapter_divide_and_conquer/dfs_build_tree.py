from typing import List


class TreeNode(object):
    """
    A node in a binary tree
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_left_child(inorder: List[int], root: TreeNode):
    """
    Finds the left child of a binary tree
    """
    idx = inorder.index(root.val)
    return inorder[:idx]


def find_right_child(inorder: List[int], root: TreeNode):
    """
    Finds the right child of a binary tree
    """
    idx = inorder.index(root.val)
    if idx >= len(inorder)-1:
        return []
    return inorder[idx+1:]


def dfs_build_tree(preorder: List = None, inorder: List = None):
    """
    dfs_build_tree
    """
    if not inorder:
        return None
    if not preorder:
        return None
    # 1.处理root
    root = TreeNode(preorder[0])

    # 2.left
    # inorder:
    left_inorder = find_left_child(inorder, root)
    root.left = dfs_build_tree(preorder=preorder[1:], inorder=left_inorder)

    # 3.right
    right_inorder = find_right_child(inorder, root)
    root.right = dfs_build_tree(preorder=preorder[2:], inorder=right_inorder)
    return root


def main():
    """Driver Code"""
    preorder = [3, 9, 2, 1, 7]
    inorder = [9, 3, 1, 2, 7]
    print(f"前序遍历 = {preorder}")
    print(f"中序遍历 = {inorder}")

    root = dfs_build_tree(preorder, inorder)
    print("构建的二叉树为：")
    # print_tree(root)
    return


if __name__ == "__main__":
    main()
