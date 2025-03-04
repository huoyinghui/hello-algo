from typing import List


class TreeNode(object):
    """
    A node in a binary tree
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "TreeNode(val={}, left={}, right={})".format(self.val, self.left, self.right)


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


def dfs_print_tree(target: int = 0, root: TreeNode = None, path: List[int] = None):
    """
    dfs_print_tree
    """
    if not root:
        return None
    path.append(root.val)
    dfs_print_tree(target=target, root=root.left, path=path)
    dfs_print_tree(target=target, root=root.right, path=path)
    return path


def dfs_find_tree_path(target: int = 0, except_target: int = 0,
                       root: TreeNode = None, path: List[int] = None, res: List = None):
    """
    dfs_find_tree_path
    """
    if not root:
        return None
    if root.val == except_target:
        return None
    path.append(root.val)
    # 是否解决，记录结果
    if root.val == target:
        res.append(list(path))
    # 遍历所有选择
    dfs_find_tree_path(target=target, except_target=except_target, root=root.left, path=path, res=res)
    dfs_find_tree_path(target=target, except_target=except_target, root=root.right, path=path, res=res)
    # 撤回
    path.pop()
    return path


def main():
    """Driver Code"""
    preorder = [3, 7, 2, 1, 7]
    inorder = [7, 3, 1, 2, 7]
    print(f"前序遍历 = {preorder}")
    print(f"中序遍历 = {inorder}")

    root = dfs_build_tree(preorder, inorder)
    path = list()
    res = list()
    dfs_find_tree_path(target=7, except_target=2, root=root, path=path, res=res)
    print("包含7的路径：", res)
    return


if __name__ == "__main__":
    main()
