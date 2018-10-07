# 先写一个MST算法

# n个点，（2，n）条边

import random
import numpy as np


def create_g1(n):
    graph = np.array([([0.00] * n) for i in range(n)])
    for i in range(n):
        for j in range(n):
            graph[i][j] = random.random()
            if i == j:
                graph[i][j] = 0
            if i > j:
                graph[i][j] = graph[j][i]
    return graph

def create_g2(n):
    dict_cor = {}
    graph = np.array([([0.00] * n) for i in range(n)])
    for i in range(n):
        dict_cor[i] = (random.random(),random.random())
    for a in range(n):
        for b in range(n):
            graph[a][b] = np.sqrt((dict_cor[a][0] - dict_cor[b][0])**2 + (dict_cor[a][1] - dict_cor[b][1])**2)
    return graph


def g_mst(g, n):
    a = []  # priority list
    for each in range(n):
        a.append(2)  # initialize priority for all edge to 2 (>1)
    pq = {}  # use dict as priority queue
    for each in range(n):
        pq[each] = a[each]  # add each edge's priority to pq
    s = []  # used to store explored node
    edge = []  # used to store mst's weight
    while pq:  # while pq is not empty
        u = min(pq, key=pq.get)  # u is the key (node) with the min value in dict (high priority)
        edge.append(pq[u])  # add u to s weight
        pq.pop(min(pq, key=pq.get))  # remove from pq
        s.append(u)  # add to s
        for u_j in range(n):
            if u_j != u:  # since this is a complete graph, all the nodes except u itself is the adjacent node of u
                if (u_j not in s) and g[u_j][u] < pq[u_j]:
                    pq[u_j] = g[u_j][u]
    return edge[1:len(edge)]  # remove the first element, which is the initial prority

def get_one_weight(n):
    g1 = create_g1(n)
    g2 = create_g2(n)
    w1 = g_mst(g1,n)
    w2 = g_mst(g2,n)
    return (sum(w1)),(sum(w2))

def get_five_ave(n):
    ave1 = 0
    ave2 = 0
    for i in range(5):
        s1 ,s2 = get_one_weight(n)
        ave1 += s1
        ave2 += s2
    return ave1/5 , ave2/5
list_n = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
def final_result(list_n):
    g1_n = []
    g2_n = []
    for each in list_n:
        ave1 ,ave2 = get_five_ave(each)
        g1_n.append(ave1)
        g2_n.append(ave2)
    return g1_n,g2_n

g1,g2 =final_result(list_n)
print(g1)
print(g2)
