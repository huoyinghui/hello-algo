"""
图的常见类型与术语

1.根据边是否具有方向
无向图（undirected graph）
    * 在无向图中，边表示两顶点之间的“双向”连接关系，例如微信或 QQ 中的“好友关系”。
有向图（directed graph）
    * 微博或抖音上的“关注”与“被关注”关系

2.根据所有顶点是否连通
连通图（connected graph）: 从某个顶点出发，可以到达其余任意顶点。
非连通图（disconnected graph）: 从某个顶点出发，至少有一个顶点无法到达。

3.根据变的权重
无权图： 所有边都一样
有权图（weighted graph)
    * 系统会根据共同游戏时间来计算玩家之间的“亲密度”


图数据结构包含以下常用术语。
邻接（adjacency）：当两顶点之间存在边相连时，称这两顶点“邻接”。在图 9-4 中，顶点 1 的邻接顶点为顶点 2、3、5。
路径（path）：从顶点 A 到顶点 B 经过的边构成的序列被称为从 A 到 B 的“路径”。在图 9-4 中，边序列 1-5-2-4 是顶点 1 到顶点 4 的一条路径。
度（degree）：一个顶点拥有的边数。对于有向图，入度（in-degree）表示有多少条边指向该顶点，出度（out-degree）表示有多少条边从该顶点指出。


图的常用表示方式包括“邻接矩阵”和“邻接表”。以下使用无向图进行举例。



邻接矩阵具有以下特性。
* 在简单图中，顶点不能与自身相连，此时邻接矩阵主对角线元素没有意义
* 对于无向图，两个方向的边等价，此时邻接矩阵关于主对角线对称。
*

使用邻接矩阵表示图时，我们可以直接访问矩阵元素以获取边，因此增删查改操作的效率很高，时间复杂度均为
 。然而，矩阵的空间复杂度为
 ，内存占用较多。



"""
from typing import List, Tuple


class GraphAdjMat:
    """
    邻接矩阵

    边的操作： 值 1/0
    顶点的操作: 行和列
    """
    def __init__(self, vertices: List[int] = None, edges: List[Tuple[int, int]] = None):
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应“顶点索引”
        self.adj_mat: list[list[int]] = []

    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        print(self.adj_mat)

    def size(self) -> int:
        """获取顶点数量"""
        return len(self.vertices)

    def add_node(self, val: int = 0):
        """
        n:0
            0*0 []

        n:1 1*1
            [0]
        n:2 2*2
            先处理行1->2: 2*1
            [0]
            [0]
            在处理列:     2*2
            [0, 0]
            [0, 0]
        n:3
            3x2 行处理 2->3
            [0, 0]
            [0, 0]
            [0, 0]

            3x3 列处理
            [0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]
        """
        n = self.size()
        # 向顶点列表中添加新顶点的值
        self.vertices.append(val)
        # 在邻接矩阵中添加一列
        new_row = [0] * n
        self.adj_mat.append(new_row)

        # 在邻接矩阵中添加一列
        for row in self.adj_mat:
            row.append(0)
        return

    def remove_node(self, val_idx: int = 0):
        """
        删除对应行，删除对应列
        """
        if val_idx not in self.vertices:
            return False
        # 通过下标删除
        self.vertices.pop(val_idx)

        # 在邻接矩阵中删除一行
        # n*n -> (n-1)*n
        self.adj_mat.pop(val_idx)

        # 在邻接矩阵中删除一列
        # (n-1)*n -> (n-1)*(n-1)
        for row in self.adj_mat:
            row.pop(val_idx)
        return

    def add_edge(self, i: int = 0, j: int = 0):
        """添加边"""
        # 参数 i, j 对应 vertices 元素索引
        # 索引越界与相等处理
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # 在无向图中，邻接矩阵关于主对角线对称，即满足 (i, j) == (j, i)
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
        return


"""Driver Code"""
if __name__ == "__main__":
    # 初始化无向图
    # vertices = [1, 3, 2, 5, 4]
    # # 请注意，edges 元素代表顶点索引，即对应 vertices 元素索引
    # edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    # graph = GraphAdjMat(vertices, edges)
    graph = GraphAdjMat()
    print("\n初始化后，图为")
    graph.add_node(1) # 0
    graph.add_node(3) # 1
    graph.add_node(5) # 2

    graph.add_node(2) # 3
    graph.add_node(4) # 4

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)

    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.add_edge(2, 4)
    # graph.add_node(2)
    # graph.remove_node(1)
    graph.print()