# -*- coding:utf-8 -*-
"""  雀魂启动  (字节跳动）"""
import copy

num = map(int, input().split())
num_map = dict([(i, 0) for i in range(1, 10)])
result = []
for i in num:
    num_map[i] += 1

# 假设添加1-9
for i in range(1, 10):
    flag = False
    if num_map[i] == 4:
        continue
    num_map[i] += 1

    # 选择雀头
    for j in range(1, 10):
        tmp = copy.copy(num_map)
        if tmp[j] < 2:
            continue
        tmp[j] -= 2

        # 判断能否胡牌
        for k in range(1, 10):

            print(tmp)

            if tmp[k] == 0:
                flag = True
                continue
            elif tmp[k] <= 2:
                k_num = tmp[k]
                val_1 = k + 1
                val_2 = k + 2
                if val_1 in tmp and val_2 in tmp and tmp[val_1] >= k_num and tmp[val_2] >= k_num:
                    flag = True
                    tmp[val_1] -= k_num
                    tmp[val_2] -= k_num
                else:
                    flag = False
                    break
            elif tmp[k] == 3:
                k_num = tmp[k]
                val_1 = k + 1
                val_2 = k + 2
                flag = True
                if val_1 in tmp and val_2 in tmp and tmp[val_1] >= k_num and tmp[val_2] >= k_num:
                    tmp[val_1] -= k_num
                    tmp[val_2] -= k_num
                else:
                    tmp[k] -= 3
            else:
                k_num = tmp[k]
                val_1 = k + 1
                val_2 = k + 2
                if val_1 in tmp and val_2 in tmp and tmp[val_1] >= k_num and tmp[val_2] >= k_num:
                    flag = True
                    tmp[val_1] -= k_num
                    tmp[val_2] -= k_num
                elif val_1 in tmp and val_2 in tmp and tmp[val_1] >= 1 and tmp[val_2] >= 1:
                    flag = True
                    tmp[val_1] -= 1
                    tmp[val_2] -= 1
                    tmp[k] -= 3
                else:
                    flag = False
                    break

        tmp = copy.copy(num_map)
        if flag:
            break

    num_map[i] -= 1

    # 收录结果
    if flag:
        result.append(i)

if len(result) == 0:
    print(0)
else:
    result = map(str, result)
    print(" ".join(result))