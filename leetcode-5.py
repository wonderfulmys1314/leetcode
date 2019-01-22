# -*- coding:utf-8 -*-

"""
    给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为 1000

    eg:
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

    输入: "cbbd"
    输出: "bb"
"""

# my soluttion can only beat 20%
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        text = ""
        # 选取长度
        for i in range(len(s), 0, -1):
            # 起始位置
            flag = False
            for head in range(0, len(s) - i + 1):
                # 尾部
                tail = head + i
                temp = s[head:tail]
                temp_inv = temp[::-1]
                if temp == temp_inv:
                    flag = True
                    text = temp

            if flag:
                break
        return text


"""
中心扩展算法:
class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        max_length = 0
        text = ""
        # 选取长度
        for i in range(2*length-1):
            # 如果为偶数
            if i%2 == 0:
                start = i//2 - 1
                end = i//2 + 1
                while start>=0 and end<length and s[start]==s[end]:
                    start -= 1
                    end += 1
                if end - start -1 > max_length:
                    max_length = end -start -1
                    text = s[start+1:end]
            else:
                start = (i-1)//2
                end = (i+1)//2
                while start >=0 and end<length and s[start]==s[end]:
                    start -= 1
                    end += 1
                if end - start - 1 > max_length:
                    max_length = end -start -1
                    text = s[start+1:end]
        return text
        

不太懂的算法：
class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        if length < 2 or s == s[::-1]: return s
        max_len, begin = 1, 0
        for i in range(1, length):
            odd = s[i - max_len - 1:i + 1]
            even = s[i - max_len:i + 1]
            if i - max_len >= 1 and odd == odd[::-1]:
                begin = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                begin = i - max_len
                max_len += 1
        return s[begin:begin + max_len]

马拉车算法:
1) 填补空隙，保证奇偶回文
2) 主要是利用回文数判断可能的半径(其实上面的问题可能也是马拉车的一种变形）
    初始化i、pos、maxRight
    遍历i得到所有可能性
    依据i和pos、maxRight的情形判断
class Solution:
    def longestPalindrome(self, s):
        mx = -1
        idx = -1
        s = '$#' + '#'.join(list(s)) + '#\0'
        argmax = -1
        max_size = -1
        p = [0]*len(s)
        for i in range(1, len(s)-1):
            # 判断是否越过边界
            if i < mx:
                p[i] = min(p[2 * idx - i], mx-i)
            else:
                p[i] = 1
            # 如果越过边界，则需要跑判断是否修改
            while s[i-p[i]] == s[i+p[i]]:
                p[i] += 1
            # 如果出现越界
            if mx < i + p[i]:
                idx = i
                mx = i + p[i]
                if p[i] > max_size:
                    max_size = p[i]
                    argmax = i
        
        return s[argmax-max_size+1: argmax+max_size].replace('#', '')
"""