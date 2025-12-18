from math import inf
import heapq

MGraph = [[inf for _ in range(7)] for _ in range(7)] # 每一个枚举
# print(len(MGraph)) # 7

def Kruskal_with_adj_matrix(MGraph):
    num_nodes = len(MGraph)  # 图中节点数量
    edges = []  # 存储所有边 (权值, 起点, 终点)
    mst_adj_matrix = [[inf for _ in range(num_nodes)] for _ in range(num_nodes)]  # 最小生成树的邻接矩阵
    mst_cost = 0  # 最小生成树的总权值

    # 初始化连通分量数组
    components = list(range(num_nodes))  # 每个节点的初始连通分量是它自己

    # 将图中的所有边加入到 edges 列表中
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # 只遍历上三角部分，避免重复
            if MGraph[i][j] != inf:
                edges.append((MGraph[i][j], i, j))  # (权值, 起点, 终点)

    # 按权值对边进行排序
    edges.sort()

    # 遍历所有边，构建最小生成树
    for weight, u, v in edges:
        if components[u] != components[v]:  # 如果两个节点不在同一个连通分量中
            # 合并两个节点的连通分量
            old_component = components[v]
            new_component = components[u]
            for i in range(num_nodes):
                if components[i] == old_component:
                    components[i] = new_component

            # 将边加入最小生成树
            mst_cost += weight  # 累加权值
            mst_adj_matrix[u][v] = weight  # 将边加入邻接矩阵
            mst_adj_matrix[v][u] = weight  # 无向图对称

    return mst_adj_matrix, mst_cost

def print_edges_from_adj_matrix(adj_matrix):
    num_nodes = len(adj_matrix)
    edges = set()  # 使用集合去重，避免重复输出无向边

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):  # 只遍历上三角部分
            if adj_matrix[i][j] != inf:  # 如果存在边
                edges.add((i, j, adj_matrix[i][j]))  # 添加边 (起点, 终点, 权值)

    # 输出边的信息
    print("最小生成树的边:")
    for edge in edges:
        print(f"起点: {edge[0]}, 终点: {edge[1]}, 权值: {edge[2]}")

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
