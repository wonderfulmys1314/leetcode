# -*- coding:utf-8 -*-

"""
	给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
	输入: "abcabcbb"
	输出: 3 
	解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3

	难点：
	""  长度为0
	" " 长度为1
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        m = 0
        length = 0
        for i, value in enumerate(s):
            if value not in d.keys():
                d[value] = i
            else:
                if d[value] >= m:
                    if length < i - m:
                        length = i - m
                    m = d[value] + 1
                else:
                    if length < i - m -1:
                        length = i - m - 1
                d[value] = i
        if length < len(s) - m:
            length = len(s) - m
        return length


"""
我的解题思路：
	创建字典，出现重复值时对字典更新最新值
	出现重复值时，依据当前头部位置判断是否需要移动指针
	最后考虑未出现重复的情形


最佳思路：
	同时创建一个空字符串，追踪当前已经遍历过的值
	根据重复的情形删除空字符串部分值(注意index(i)操作）
	记录最大值
"""
