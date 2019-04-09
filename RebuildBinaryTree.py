# -*- coding:utf-8 -*-

"""
    通过前序和中序重构二叉树
"""

import sys

line = sys.stdin.readline().strip().split(" ")
forward = list(map(int, line))
line = sys.stdin.readline().strip().split(" ")
middle = list(map(int, line))


# 定义节点
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getBinaryTree(forward, middle):
    """
    :param forward: 先序遍历
    :param middle: 中序遍历
    :return:
        返回根节点
    """
    # 剩余节点数
    length = len(forward)

    # 如果剩余一个节点
    if length == 1:
        return Node(forward[0])
    else:
        value = forward[0]
        root = Node(value)
        # 找到区分位置
        index = 0
        while middle[index] != value:
            index += 1

        # 判断可能的情况
        if index==0:
            root.left = None
            root.right = getBinaryTree(forward[1:length], middle[1:length])
        elif index==length-1:
            root.right = None
            root.left = getBinaryTree(forward[1:length], middle[0:length-1])
        else:
            root.left = getBinaryTree(forward[1:index+1], middle[0:index])
            root.right = getBinaryTree(forward[index+1:length], middle[index+1:length])

        return root


root = getBinaryTree(forward, middle)


def show(root):
    if root is None:
        pass
    else:
        print(root.value)
        show(root.left)
        show(root.right)

show(root)