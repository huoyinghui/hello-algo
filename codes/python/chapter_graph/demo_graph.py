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
    """
    def __init__(self, vertices: List[int] = None, edges: List[Tuple[int, int]] = None):
        # 保存顶点
        self.vertices = vertices
        self.matrix = [[0 for _ in self.vertices] for _ in self.vertices]
        # 保存边
        self.edges = edges
        for u_idx, v_idx in edges:
            self.matrix[u_idx][v_idx] = 1

    def __str__(self):
        print(f"ver: {self.vertices}")
        for row in self.matrix:
            print(f"row: {row}")
        return ""


"""Driver Code"""
if __name__ == "__main__":
    # 初始化无向图
    vertices = [1, 3, 2, 5, 4]
    # 请注意，edges 元素代表顶点索引，即对应 vertices 元素索引
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMat(vertices, edges)
    print("\n初始化后，图为")
    print(graph)