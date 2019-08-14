# -*- coding:utf-8 -*-
from collections import Counter

line = list(map(int, input().split()))
N = line[0]
K = line[1]
number_input = input()
d = Counter(list(map(int, number_input)))
res = float("inf")
ans = "X"

for i in range(10):
    tmp = number_input
    cost = 0
    dist = 1
    need = K - d[i]
    while need > 0:
        if i + dist <= 9:
            if d[i + dist] < need:
                need -= d[i + dist]
                cost += dist * d[i + dist]
                tmp = tmp.replace(str(i+dist), str(i))
            else:
                cost += dist * need
                tmp = tmp.replace(str(i+dist), str(i), need)
                break
        if i - dist >= 0:
            if d[i - dist] < need:
                need -= d[i - dist]
                cost += dist * d[i - dist]
                tmp = tmp.replace(str(i-dist), str(i))
            else:
                tmp_s = tmp[::-1]
                tmp_s = tmp_s.replace(str(i-dist), str(i), need)
                cost += need * dist
                tmp = tmp_s[::-1]
                break
        dist += 1

    if cost < res:
        res = cost
        ans = tmp
    elif cost == res and tmp < ans:
        ans = tmp

print(res)
print(ans)
