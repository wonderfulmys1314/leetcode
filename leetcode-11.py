# -*- coding:utf-8 -*-
"""
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

    说明：你不能倾斜容器，且 n 的值至少为 2。

    图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

"""

"""
    主要还是需要观察出变化的特点，
    有点意思吧
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        # 初始值
        value = 0
        while i<j:
            # 此时最小值
            a = min(height[i], height[j])
            value = max((j-i)*a, value)
            while i<j and height[i] <= a:
                i += 1
            while i<j and height[j] <= a:
                j -= 1
        return value