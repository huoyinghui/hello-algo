class HeapTree:
    """
    “二叉树”章节讲过，完全二叉树非常适合用数组来表示。由于堆正是一种完全二叉树，因此我们将采用数组来存储堆。

当使用数组表示二叉树时，元素代表节点值，索引代表节点在二叉树中的位置。节点指针通过索引映射公式来实现。

如图 8-2 所示，给定索引 
 ，其左子节点的索引为 
 ，右子节点的索引为 
 ，父节点的索引为 
（向下整除）。当索引越界时，表示空节点或节点不存在
    """
    def left(self, i: int) -> int:
        """获取左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """获取右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取父节点的索引"""
        return (i - 1) // 2  # 向下整除

    def peek(self) -> int:
        """访问堆顶元素"""
        return self.max_heap[0]

def main():
    pass


if __name__ == "__main__":
    main()

