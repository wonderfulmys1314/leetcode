# -*- coding:utf-8 -*-

""" 方法一：查找所有可能的组合方式 """


# # 文件版本
# in_path = "data/A-small-practice-1.in"
# out_path = "result/A-small-practice-1_first.out"
#
# f_in = open(in_path, "r")
# f_out = open(out_path, "w")
#
# T = int(f_in.readline().strip())
#
# # 读取样例
# for t in range(T):
#     M = int(f_in.readline().strip())
#     pre_result = [([], [])]
#     flag = "Yes"
#
#     # 读取内容
#     for m in range(M):
#         # 读取新的一行
#         line = f_in.readline().strip().split()
#         update_result = []
#
#         # 是否不再需要继续深入分析
#         if flag == "No":
#             continue
#
#         # 更新组合
#         for result in pre_result:
#             # 如果同时出现在一个集合，跳过
#             if (line[0] in result[0] and line[1] in result[0]) or (line[0] in result[1] and line[1] in result[1]):
#                 continue
#
#             # 如果出现在两边，保留
#             elif (line[0] in result[0] and line[1] in result[1]) or (line[1] in result[0] and line[0] in result[1]):
#                 update_result.append((result[0], result[1]))
#
#             # 如果只有一个出现过
#             elif line[0] in result[0]:
#                 result[1].append(line[1])
#                 update_result.append((result[0], result[1]))
#             elif line[0] in result[1]:
#                 result[0].append(line[1])
#                 update_result.append((result[0], result[1]))
#             elif line[1] in result[0]:
#                 result[1].append(line[0])
#                 update_result.append((result[0], result[1]))
#             elif line[1] in result[1]:
#                 result[0].append(line[0])
#                 update_result.append((result[0], result[1]))
#
#             # 如果都没有出现
#             else:
#                 update_result.append((result[0] + [line[0]], result[1] + [line[1]]))
#                 update_result.append((result[0] + [line[1]], result[1] + [line[0]]))
#
#         if len(update_result) == 0:
#             flag = "No"
#         else:
#             # 更新
#             pre_result = update_result
#
#     #   输出结果
#     f_out.write("Case #%d: %s"%(t+1, flag))
#     f_out.write("\n")


""" 
    只要是连通的，有状态便可以接上去
"""


# 文件版本
in_path = "data/A-small-practice-2.in"
out_path = "result/A-small-practice-2.out"

f_in = open(in_path, "r")
f_out = open(out_path, "w")

T = int(f_in.readline().strip())

# 读取样例
for t in range(T):
    M = int(f_in.readline().strip())
    d = {}
    visited = {}
    YES = True

    # 读取内容
    for m in range(M):
        line = f_in.readline().strip().split()
        d.setdefault(line[0], []).append(line[1])
        d.setdefault(line[1], []).append(line[0])
        visited[line[0]] = -1
        visited[line[1]] = -1

    if t == 0:
        print(d)
        print(visited)

    # 遍历
    for key in d.keys():
        # 是否访问过
        if visited[key] == -1:
            visited[key] = 0
        # else:
        #     continue

        # 广度搜索
        result = [key]

        while len(result) > 0:
            if t == 0:
                print("-----------------")
                print(result)
                print(visited)
                print("-----------------")
            # 选取初始结点，寻找子节点
            init_key = result.pop(0)
            # 判断子节点是否满足条件，不冲突
            for next_key in d[init_key]:
                # 如果没有遍历过
                if visited[next_key] == -1:
                    visited[next_key] = int(1 - visited[init_key])
                    result.append(next_key)
                # 如果已经设置过且出现冲突
                elif visited[next_key] == visited[init_key]:
                    YES = False
                    break
                else:
                    continue

            if not YES:
                break

        if not YES:
            break

    # print(YES)
    # print(t)
    if YES:
        f_out.write("Case #%d: Yes" % (t + 1))
    else:
        f_out.write("Case #%d: No" % (t + 1))
    f_out.write("\n")




