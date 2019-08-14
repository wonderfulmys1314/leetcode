# -*- coding:utf-8 -*-


N = int(input())
line = list(map(int, input().split()))
class_index = {}
M = 0

# 统计类别数目
for i, value in enumerate(line):
    class_index[i+1] = value
    M += value

# print(class_index)
# 初始状态
init_state = [1]
class_index[1] -= 1
# 临界值
class_index[N+1] = -1

while len(init_state) > 0:
    # print(init_state)
    # print(class_index)

    # 存在合理方案
    if len(init_state) == M:
        break

    # 从最小值开始添加
    init_state.append(1)
    class_index[1] -= 1

    while True:
        # 如果长度为1
        if len(init_state) == 1:
            if init_state[0] == N + 1:
                init_state.pop()
            break

        # 满足条件
        if class_index[init_state[-1]] >= 0 and init_state[-1] != init_state[-2]:
            break
        # 不满足条件时
        # 没超过界限，更新
        if init_state[-1] != N + 1:
            class_index[init_state[-1]] += 1
            init_state[-1] += 1
            class_index[init_state[-1]] -= 1
        # 超过界限，回溯
        else:
            class_index[init_state[-1]] += 1
            init_state.pop()
            class_index[init_state[-1]] += 1
            init_state[-1] += 1
            class_index[init_state[-1]] -= 1

# print(len(init_state))
if len(init_state) == M:
    print(" ".join(map(str, init_state)))
else:
    print("-")