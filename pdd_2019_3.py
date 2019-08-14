# -*- coding:utf-8 -*-

"""  两两配对  """
from collections import Counter

n = int(input())
number = list(map(int, input().split()))
d = Counter(number)
keys = list(d.keys())
keys = sorted(keys, reverse=False)

number_input = []

for key in keys:
    number_input.extend(d[key] * [key])

count = 0
half = n / 2
max_sum = 0
min_sum = float("inf")
i = 0
j = n - 1

while i < j:
    max_sum = max(max_sum, number_input[i] + number_input[j])
    min_sum = min(min_sum, number_input[i] + number_input[j])
    i += 1
    j -= 1

print(max_sum-min_sum)
