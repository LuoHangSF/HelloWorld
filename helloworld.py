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

print("hello world")
