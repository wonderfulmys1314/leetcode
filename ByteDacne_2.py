line = list(map(int, input().split()))
N = line[0]
K = line[1]
s = [int(i) for i in input()]

# 记录结果
res = []
# 前面的计算结果
pre = 0


for i in range(K+N-1):
    if i < K:
        pre = pre ^ s[i]
        res.append(pre)
        pre = s[i]
    else:
        pre = s[i-1] ^ res[i-K]
        res.append(pre ^ s[i])

    if len(res) == N:
        break

print("".join(map(str, res)))








