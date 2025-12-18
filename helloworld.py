from math import inf
MGraph = [[inf for _ in range(7)] for _ in range(7)] # 每一个枚举
# print(len(MGraph)) # 7

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
