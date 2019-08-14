""" 挑选最多两个叶子节点 """

limit = int(input())
city = int(input())

# 子节点、父节点以及距离
sons = [[] for _ in range(city)]
parent = [-1 for _ in range(city)]
dist = [[0] * city for _ in range(city)]

for i in range(city-1):
    line = list(map(int, input().split()))
    sons[line[0]].append(line[1])
    parent[line[1]] = line[0]
    dist[line[0]][line[1]] = line[2]

# 寻找根节点
root = None
for i in range(city):
    if parent[i] == -1:
        root = i


# 深度优先
def dfs(root):
    """
        按道理，有三种可能
            不继续深度时的长度
            只探索一个子节点
            探索两个子节点
        返回的是所有可能的长度
    """
    res = set()
    # 不探索时的长度
    res.add(0)

    # 如果没有子节点，直接返回
    if len(sons[root]) == 0:
        return res

    select_son = []
    select_res = []

    # 遍历子节点，存储相应的子节点以及最大长度
    for son in sons[root]:
        select_son.append(son)
        select_res.append(dfs(son))

    # 在限制条件下的最大长度
    for i in range(len(select_son)):
        # 选择一个子节点
        d_1 = dist[root][select_son[i]]
        for dist_1 in select_res[i]:
            if d_1 + dist_1 <= limit:
                res.add(d_1+dist_1)
            # 选择两个子节点
            for j in range(i+1, len(select_son)):
                d_2 = dist[root][select_son[j]]
                for dist_2 in select_res[j]:
                    if d_1 + d_2 + dist_1 + dist_2 <= limit:
                        res.add(d_1 + d_2 + dist_1 + dist_2)
    return res


print(max(dfs(root)))













