from collections import Counter

N = int(input())
line = list(map(int, input().split()))
flag = [False] * N
d = Counter(line)
keys = sorted(list(d.keys()), reverse=False)

start = 100
all_money = 0
count = 0

if N == 1:
    print(100)
else:
    while count < N:
        index = 0
        for i in range(len(line)):
            if flag[i]:
                continue
            else:
                if i == 0 and line[i] <= line[i+1]:
                    index += 1
                    flag[i] = True
                    all_money += start
                elif i == len(line) - 1 and line[i-1]>line[i]:
                    index += 1
                    flag[i] = True
                    all_money += start
                else:
                    if line[i] <= line[i-1] and line[i] <= line[i+1]:
                        index += 1
                        all_money += start
                        flag[i] = True
        if index == 0:
            all_money += start * (N-count)
            break
        start += 100
        count += index

    print(all_money)






