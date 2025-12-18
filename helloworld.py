from math import inf
import heapq

MGraph = [[inf for _ in range(7)] for _ in range(7)] # 每一个枚举
# print(len(MGraph)) # 7

def Prim_with_adj_matrix(MGraph, start):
    num_nodes = len(MGraph)  # 图中节点数量
    visited = [False] * num_nodes  # 记录节点是否已加入最小生成树
    min_heap = []  # 最小堆，存储候选边 (权值, 起点, 终点)
    mst_cost = 0  # 最小生成树的总权值

    # 初始化最小生成树的邻接矩阵
    mst_adj_matrix = [[inf for _ in range(num_nodes)] for _ in range(num_nodes)]

    # 将起始节点的所有边加入堆
    visited[start] = True
    for end in range(num_nodes):
        if MGraph[start][end] != inf:
            heapq.heappush(min_heap, (MGraph[start][end], start, end)) # (权值, 起点, 终点)

    # 不断扩展最小生成树
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)  # 弹出权值最小的边
        if visited[v]:
            continue  # 如果终点已在最小生成树中，跳过
        visited[v] = True  # 标记终点已加入最小生成树
        mst_cost += weight  # 累加权值

        # 将边加入最小生成树的邻接矩阵
        mst_adj_matrix[u][v] = weight
        mst_adj_matrix[v][u] = weight  # 无向图对称

        # 将新节点的所有边加入堆
        for next_node in range(num_nodes):
            if not visited[next_node] and MGraph[v][next_node] != inf:
                heapq.heappush(min_heap, (MGraph[v][next_node], v, next_node))

    return mst_adj_matrix, mst_cost

print("hello world")