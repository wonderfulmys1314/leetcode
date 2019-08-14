# -*- coding:utf-8 -*-

""" 字节跳动 后台开发 """

line = list(map(int, input().split()))

n = line[0]
m = line[1]
c = line[2]

color_index = {}

# 记录颜色位置
for i in range(n):
    line = list(map(int, input().split()))

    # 如果是无色的，跳过
    if line[0] == 0:
        continue

    # 如果有颜色，记录颜色位置
    for j in range(line[0]):
        color_index.setdefault(line[j+1], []).append(i)

# 判断是否重复
count = 0
for key in color_index.keys():
    index_list = color_index[key]
    flag = False
    # 求前后间距
    for i in range(len(index_list)):
        if i == len(index_list) - 1:
            dist = index_list[0] + n - index_list[-1]
        else:
            dist = index_list[i+1] - index_list[i]
        if dist < m:
            flag = True
            break
    if flag:
        count += 1

print(count)


