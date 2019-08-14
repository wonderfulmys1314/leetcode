# -*- coding:utf-8 -*-

n = int(input())
extra = 1024 - n
value = [1, 4, 16, 64]
count = 0

for i in range(3, -1, -1):
    num = extra // value[i]
    count += num
    extra -= num * value[i]
    if extra == 0:
        break

print(count)