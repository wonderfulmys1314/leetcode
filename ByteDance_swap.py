# -*- coding:utf-8 -*-

line = input().split()
s = line[0]
m = int(line[1])

alpha_index = {}

# 统计
for i in range(len(s)):
    alpha_index.setdefault(s[i], []).append(i)


#
