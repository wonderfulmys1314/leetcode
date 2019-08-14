# while True:
line = input().strip().split()
line = list(map(int, line))

offset = line[0]
n = line[1]
l1_length = line[2]
l2_length = line[3]
result = []

start = offset
end = offset + n
all_length = l1_length + l2_length

if end <= l1_length:
    print(" ".join(map(str, [start, end, 0, 0])))
elif start <= l1_length and end <= all_length:
    print(" ".join(map(str, [start, l1_length, 0, end-l1_length])))
elif start > l1_length and end <= all_length:
    print(" ".join(map(str, [l1_length, l1_length, start-l1_length, end - l1_length])))
elif start <= l1_length and end > all_length:
    print(" ".join(map(str, [start, l1_length, 0, l2_length])))
elif end > all_length >= start:
    print(" ".join(map(str, [l1_length, l1_length, start - l1_length, l2_length])))
else:
    print(" ".join(map(str, [l1_length, l1_length, l2_length, l2_length])))
