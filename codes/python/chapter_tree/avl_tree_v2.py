
"""
在“二叉搜索树”章节中我们提到，在多次插入和删除操作后，二叉搜索树可能退化为链表。在这种情况下，所有操作的时间复杂度将从logn劣化为On

节点平衡因子: 节点左子树的高度减去右子树的高度，同时规定空节点的平衡因子为0
"""


class TreeNode:
    """AVL 树节点类"""
    def __init__(self, val: int):
        self.val: int = val                 # 节点值
        self.height: int = 0                # 节点高度
        self.left: TreeNode | None = None   # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用

    @property
    def is_leaf(self) -> bool:
        """
        是否是叶子节点
        """
        if self.left:
            return False
        if self.right:
            return False
        return True


class AVLTree:
    """
    AVL 树的特点在于“旋转”操作，它能够在不影响二叉树的中序遍历序列的前提下，使失衡节点重新恢复平衡。换句话说，旋转操作既能保持“二叉搜索树”的性质，也能使树重新变为“平衡二叉树”。
    我们将平衡因子绝对值>1的节点称为“失衡节点”。
    根据节点失衡情况的不同，旋转操作分为四种：右旋、左旋、先右旋后左旋、先左旋后右旋。
    """

    def height(self, node: TreeNode | None) -> int:
        """
        获取节点高度
        节点高度”是指从该节点到它的最远叶节点的距离，即所经过的“边”的数量。需要特别注意的是，叶节点的高度为0，而空节点的高度为-1
        """
        # 空节点高度为 -1 ，叶节点高度为 0
        if not node:
            return -1
        if node.is_leaf:
            return 0
        return node.height

    def update_height(self, node: TreeNode | None) -> int:
        """
        节点高度等于最高子树高度 + 1
        """
        return max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node: TreeNode | None) -> int:
        """
        平衡因子（balance factor)
        定义为节点左子树的高度减去右子树的高度，同时规定空节点的平衡因子为 0

        失衡节点： 平衡因子绝对值>1, 需要旋转
        """
        if not node:
            return 0
        # 节点平衡因子 = 左子树高度 - 右子树高度
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
        pass

    def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
        pass
