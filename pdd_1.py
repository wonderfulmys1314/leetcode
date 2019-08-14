N = int(input())
number = list(map(int, input().split()))
res = float("inf")
number = sorted(number, reverse=False)


def cal_res(a, b, c):
    m = sum([a, b, c])/3
    std = ((a-m)**2 + (b-m)**2 + (c-m)**2)/3
    return std


for i in range(1, N-2):
    res = min(res, cal_res(number[i-1], number[i], number[i+1]))

print("%.2f"%res)