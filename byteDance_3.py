# -*- coding:utf-8 -*-

"""
    城市旅游 tsp问题
    动态规划的模型  dp[i][j]
        i 表示城市状态 j表示出发的顶点 其中j在城市集合中
"""

n = int(input())
dist = []
for i in range(n):
    dist.append(list(map(int, input().split())))


def tsp_1(dist, n):
    """
        从那座城市出发的结果应该一致，不妨假设从城市0出发
        dp表示从顶点i出发，经过集合中的城市最后回到城市0的距离，集合中的城市不应该包括0和i
    """
    state_num = 1 << n
    dp = [[float("inf")] * n for i in range(state_num)]

    # 初始状态，回到城市0的距离
    for i in range(n):
        dp[0][i] = dist[i][0]

    # 城市集合状态变化
    for i in range(1, state_num):
        # 包括城市0的集合不讨论
        if i & 1:
            continue
        # 新的出发结点，不在集合中
        for j in range(n):
            if i & (1 << j) == 0:
                # 先前的出发结点，在集合中
                for k in range(1, n):
                    if i & (1 << k):
                        dp[i][j] = min(dp[i][j], dp[i-(1<<k)][k]+dist[j][k])

    res = float("inf")
    for i in range(n):
        res = min(res, dp[(1<<n)-(1<<i)-1][i] + dist[0][i])

    return res


# print(tsp_1(dist, n))

def tsp_2(dist, n):
    """ 贪心算法 """

    # 起始点
    for i in range(n):
        # 距离
        sum = 0
        # 状态
        s = [-1 for _ in range(n)]
        # 路径
        path = [-1 for _ in range(n)]

        # 起始状态
        s[i] = 1
        path[0] = i

        # 遍历接下来的路径
        for j in range(1, n):
            tmp = float("inf")
            select = 0
            # 寻找最近的城市
            for k in range(n):
                # 未访问过
                if s[k] == -1:
                    # 寻找最近的城市
                    if dist[path[j - 1]][k] < tmp:
                        tmp = dist[path[j - 1]][k]
                        select = k
            # print("s ", s)
            # print("path ", path)
            # print("sum ", sum)
            s[select] = 1
            path[j] = select
            sum += tmp

        print(sum+dist[path[-1]][i], path)


tsp_2(dist, n)









