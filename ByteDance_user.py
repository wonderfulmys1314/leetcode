# # -*- coding:utf-8 -*-
#
# """ 用户爱好  字节跳动2018后端 """
#
# user_num = int(input())
# user_k = list(map(int, input().split()))
# q = int(input())
# index = 1
#
# while index <= q:
#     users = list(map(int, input().split()))
#     l = users[0]
#     r = users[1]
#     k = users[2]
#
#     count = 0
#     for i in range(l-1, r):
#         if user_k[i] == k:
#             count += 1
#     print(count)
#     index += 1

n = int(input())

scores = list(map(int, input().split()))

dict_index = {}

for index, value in enumerate(scores):
    dict_index.setdefault(value, []).append(index+1)


q = int(input())

for j in range(0, q):

    q_list = list(map(int, input().split()))

    if q_list[2] not in dict_index:
        print(0)
        continue

    index_list = dict_index[q_list[2]]

    count = 0

    # 用户范围和查询数组求交集

    for i in index_list:

        if q_list[0] <= i <= q_list[1]:

            count += 1

    print(count)
