import sys

line = input().strip().split(" ")


def combination(line, s):
    if len(line)==0:
        if s!="":
            print(s)
    else:
        combination(line[1:], s)
        s += line[0]
        combination(line[1:], s)


combination(line, "")