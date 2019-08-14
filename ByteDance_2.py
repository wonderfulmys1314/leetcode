# -*- coding-utf-8 -*-

""" 寻找猫的特征 """

n_sample = int(input())
# print(n_sample)
result = []
index = 1

while index <= n_sample:
    m_frames = int(input())
    # print(m_frames)
    cats_dict = dict()
    count = 0
    for frame in range(m_frames):
        line = list(map(int, input().split()))
        # print(line)
        num = line[0]
        cats = [(line[i*2+1], line[i*2+2]) for i in range(num)]
        # print(cats)
        pre_cats = list(cats_dict.keys())
        extra_cats = set(pre_cats) - set(cats)
        for extra_cat in extra_cats:
            if extra_cat in cats_dict:
                del cats_dict[extra_cat]
        for i in range(num):
            if cats[i] not in cats_dict:
                cats_dict[cats[i]] = 1
            else:
                cats_dict[cats[i]] += 1
            count = max(count, cats_dict[cats[i]])
        # print(count)
    index += 1
    result.append(count)

result = map(str, result)
print("\n".join(result))