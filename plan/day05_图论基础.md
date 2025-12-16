# 第5天：图论基础

## 📚 学习目标
掌握图的基本概念、表示方法和遍历算法，能够解决基础的图论问题。

## 🔍 核心知识点

### 上午：图的基础概念与表示

#### 1. 图的基本概念
- **定义**：由顶点（Vertex）和边（Edge）组成的数据结构
- **表示法**：G = (V, E)，其中V是顶点集合，E是边集合
- **基本术语**：
  - 有向图 vs 无向图
  - 带权图 vs 无权图
  - 有环图 vs 无环图（DAG）
  - 连通图 vs 非连通图
  - 出度、入度
  - 路径、简单路径、环

#### 2. 图的表示方法

##### 邻接矩阵（Adjacency Matrix）
- **定义**：n×n的二维数组表示图
- **特点**：
  - 适合稠密图
  - 查找边：O(1)
  - 空间复杂度：O(n²)
  - 判断两点是否相邻快速

```python
# 邻接矩阵表示
adj_matrix = [
    [0, 1, 0, 1],  # 顶点0的邻接情况
    [1, 0, 1, 0],  # 顶点1的邻接情况
    [0, 1, 0, 1],  # 顶点2的邻接情况
    [1, 0, 1, 0]   # 顶点3的邻接情况
]
```

##### 邻接表（Adjacency List）
- **定义**：每个顶点维护一个邻接顶点的链表/数组
- **特点**：
  - 适合稀疏图
  - 查找边：O(度)
  - 空间复杂度：O(n + e)
  - 节省空间

```python
# 邻接表表示
adj_list = {
    0: [1, 3],     # 顶点0的邻接顶点
    1: [0, 2],     # 顶点1的邻接顶点
    2: [1, 3],     # 顶点2的邻接顶点
    3: [0, 2]      # 顶点3的邻接顶点
}
```

### 下午：图的遍历算法

#### 1. 深度优先搜索（DFS）
- **思想**：一路走到黑，撞墙再回头
- **实现**：使用栈（递归或显式栈）
- **应用**：
  - 查找路径
  - 检测环
  - 拓扑排序
  - 强连通分量

```python
def dfs(graph, node, visited):
    visited.add(node)
    # 处理当前节点
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

#### 2. 广度优先搜索（BFS）
- **思想**：层层扩展，像水波一样
- **实现**：使用队列
- **应用**：
  - 最短路径（无权图）
  - 连通性检查
  - 二分图判断

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        # 处理当前节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

#### 3. 遍历算法对比
| 特性 | DFS | BFS |
|------|-----|-----|
| 数据结构 | 栈 | 队列 |
| 空间复杂度 | O(h) | O(w) |
| 最短路径 | ❌ | ✅（无权图） |
| 应用场景 | 路径存在、拓扑排序 | 最短路径、连通分量 |

## 📁 相关代码文件
- 图的实现：
  - `codes/python/chapter_graph/graph_adjacency_list.py`
  - `codes/python/chapter_graph/graph_adjacency_matrix.py`
  - `codes/go/chapter_graph/`

## 📖 推荐阅读文档
- `docs/chapter_graph/`

## 💻 动手实践

### 练习1：实现图的邻接矩阵
要求：
1. 实现有向图和无向图
2. 支持添加/删除边
3. 支持权重设置
4. 实现度数计算

### 练习2：实现图的邻接表
要求：
1. 使用字典+列表实现
2. 对比邻接矩阵的优缺点
3. 实现基本的图操作

### 练习3：实现DFS和BFS
要求：
1. 递归和非递归版本的DFS
2. 使用队列实现BFS
3. 记录遍历路径
4. 计算连通分量

### 练习4：图的应用
要求：
1. 检测图中是否有环
2. 找出两点间的路径
3. 计算无权图的最短路径

## 🎯 晚上刷题（LeetCode）

### 基础图类题目
1. **[1971. 寻找图中是否存在路径](https://leetcode.cn/problems/find-if-path-exists-in-graph/)**
   - 难度：简单
   - 考点：DFS/BFS基础

2. **[797. 所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)**
   - 难度：中等
   - 考点：DFS回溯

3. **[200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)**
   - 难度：中等
   - 考点：DFS/BFS遍历

4. **[994. 腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/)**
   - 难度：中等
   - 考点：BFS多源搜索

### 进阶图类题目
1. **[130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)**
   - 难度：中等
   - 考点：DFS标记

2. **[133. 克隆图](https://leetcode.cn/problems/clone-graph/)**
   - 难度：中等
   - 考点：图遍历+哈希表

3. **[207. 课程表](https://leetcode.cn/problems/course-schedule/)**
   - 难度：中等
   - 考点：拓扑排序、DFS检测环

4. **[210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/)**
   - 难度：中等
   - 考点：拓扑排序

5. **[127. 单词接龙](https://leetcode.cn/problems/word-ladder/)**
   - 难度：困难
   - 考点：BFS最短路径

## ✅ 掌握标准
- [ ] 理解图的基本概念和术语
- [ ] 掌握邻接矩阵和邻接表的实现
- [ ] 熟练实现DFS和BFS遍历
- [ ] 理解两种遍历算法的适用场景
- [ ] 能解决基础的图论问题
- [ ] 掌握拓扑排序的概念和应用

## 📝 学习笔记
### 重点记录
1. 邻接矩阵vs邻接表的选择标准
2. DFS的递归和迭代实现技巧
3. BFS层序遍历的特点
4. 图的连通性判断方法
5. 环检测的不同方法

### 常见错误
1. 忘记标记已访问节点导致无限循环
2. 邻接表的初始化错误
3. DFS递归深度过大（考虑迭代实现）
4. BFS队列操作顺序错误
5. 有向图和无向图的处理混淆

### 实用技巧
1. 使用visited集合避免重复访问
2. BFS可以求最短路径（无权图）
3. DFS可以求拓扑排序
4. 颜色标记法判断二分图
5. 并查集处理连通性问题

### 进阶拓展
1. 最小生成树（Prim、Kruskal）
2. 最短路径（Dijkstra、Bellman-Ford、Floyd）
3. 强连通分量（Tarjan、Kosaraju）
4. 二分图最大匹配（匈牙利算法）
5. 网络流（Ford-Fulkerson）