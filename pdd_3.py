line = list(map(int, input().split()))
n = line[0]
s = line[1]
count = 0
res = [1]

while len(res) > 0:
    # 到达指定长度
    if len(res) == n:
        if sum(res) == s:
            count += 1
            res.pop()
            res[-1] += 1
        else:
            res[-1] += 1

    else:
        # 进栈
        last_value = res[-1]
        res.append(last_value+1)

        if sum(res) > s and len(res) <= 3:
            break

        while sum(res) > s:
            res.pop()
            if len(res) == 0:
                break
            res[-1] += 1

print(count%1000000007)



