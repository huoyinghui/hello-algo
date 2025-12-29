from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AVLTreeNode:
    """
    AVL 树节点类
    AVL 树的特点在于“旋转”操作，它能够在不影响二叉树的中序遍历序列的前提下，使失衡节点重新恢复平衡。换句话说，旋转操作既能保持“二叉搜索树”的性质，也能使树重新变为“平衡二叉树”。
    我们将平衡因子绝对值>1的节点称为“失衡节点”。
    
    根据节点失衡情况的不同，旋转操作分为四种：右旋、左旋、先右旋后左旋、先左旋后右旋。下面详细介绍这些旋转操作。

    """
    def __init__(self, val: int):
        self.val: int = val                 # 节点值
        self.height: int = 0                # 节点高度. 是指从该节点到它的最远叶节点的距离，即所经过的“边”的数k 
        self.left: TreeNode | None = None   # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用
    
    def height(self, node: TreeNode | None) -> int:
        """获取节点高度"""
        # 空节点高度为 -1 ，叶节点高度为 0
        if node is not None:
            return node.height
        return -1
    
    def update_height(self, node: TreeNode | None):
        """更新节点高度"""
        # 节点高度等于最高子树高度 + 1
        node.height = max([self.height(node.left), self.height(node.right)]) + 1
        return

    def balance_factor(self, node: TreeNode | None) -> int:
        """获取平衡因子"""
        # 空节点平衡因子为 0
        if node is None:
            return 0
        # 节点平衡因子 = 左子树高度 - 右子树高度
        return self.height(node.left) - self.height(node.right)



# 前序遍历
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# 中序遍历
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# 后序遍历
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

# 层序遍历
def levelorder(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        # 模拟队列操作.  右边append, 左边pop
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result