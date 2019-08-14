# -*- coding:utf-8 -*-

import sys

str_number = sys.stdin.readline().strip()
length = len(str_number)


def cal_one(str_number, length):
    if length==1 and str_number[0]=='0':
        return 0
    elif length==1:
        return 1
    elif str_number[0]=="1":
        return cal_one(str_number[1:], length-1) + int(str_number[1:]) + 1 + 10**(length-2) * (length-1)
    else:
        return cal_one(str_number[1:], length-1) + 10 ** (length-1) + 10 ** (length - 2) * (length - 1)


result = cal_one(str_number, length)
print(result)
