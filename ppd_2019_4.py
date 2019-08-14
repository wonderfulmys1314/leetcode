HP = int(input())
nA = int(input())
bA = int(input())

import math

if nA * 2 >= bA:
    count = math.ceil(HP / nA)
else:
    res = HP // bA
    extra = HP % bA
    count = 2 * res + min(math.ceil(extra/nA), 2)

print(count)

