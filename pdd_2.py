line = list(map(int, input().split()))
L = line[0]
N = line[1]
numbers = list(map(int, input().split()))
min_dist = float("inf")
select = 0

# 遍历
for i in range(L):
    dist = 0
    # 针对每一个点选择合适的方向
    for number in numbers:
        if i < number:
            tmp = min(number-i, i+L-number)
            dist += tmp
        else:
            tmp = min(i-number, L-i+number)
            dist += tmp

    if dist < min_dist:
        min_dist = min(min_dist, dist)
        select = i


if select in numbers:
    print(min_dist-N-1)
else:
    print(min_dist-N)