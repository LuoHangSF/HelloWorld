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


if __name__ == '__main__':
    print("hello world")
    MGraph[1][2] = 20
    MGraph[1][5] = 10
    MGraph[1][6] = 9
    
    MGraph[2][1] = 20
    MGraph[2][3] = 5
    MGraph[2][4] = 6
    MGraph[2][6] = 11
    
    MGraph[3][2] = 5
    MGraph[3][4] = 6
    
    MGraph[4][2] = 6
    MGraph[4][3] = 6
    MGraph[4][5] = 10
    MGraph[4][6] = 14
    
    MGraph[5][1] = 10
    MGraph[5][4] = 10
    MGraph[5][6] = 10
    
    MGraph[6][1] = 9
    MGraph[6][2] = 11
    MGraph[6][4] = 14
    MGraph[6][5] = 10
    
    # 调用 Prim 算法
    print("=================== Prim ==================")
    start_node = 1
    mst_adj_matrix, mst_cost = Prim_with_adj_matrix(MGraph, start_node)

    # 输出最小生成树的邻接矩阵
    print("最小生成树的总权值:", mst_cost)
    # print("最小生成树的邻接矩阵:")
    # for row in mst_adj_matrix:
    #     print(row)
        
    # 调用函数输出最小生成树的边
    print_edges_from_adj_matrix(mst_adj_matrix)
    
    # 调用 Kruskal 算法
    print("=================== Kruskal ==================")
    mst_adj_matrix_k, mst_cost_k = Kruskal_with_adj_matrix(MGraph)
    # 输出最小生成树的邻接矩阵
    print("最小生成树的总权值:", mst_cost_k)
    # print("最小生成树的邻接矩阵:")
    # for row in mst_adj_matrix_k:
        # print(row)
    # 调用函数输出最小生成树的边
    print_edges_from_adj_matrix(mst_adj_matrix_k)
