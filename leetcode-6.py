# -*- coding:utf-8 -*-

"""
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

    比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

    L   C   I   R
    E T O E S I I G
    E   D   H   N
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

    请你实现这个将字符串进行指定行数变换的函数：

    string convert(string s, int numRows);
    示例 1:

    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"
    示例 2:

    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"
    解释:

    L     D     R
    E   O E   I I
    E C   I H   N
    T     S     G
"""


# 我的思考还是没有考虑到例外情况，这个问题一定要注意
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 依据行数判断生成Z字形需要的字符
        if numRows == 1:
            return s
        z_all = numRows*2-2
        result = ["" for i in range(numRows)]
        for i, value in enumerate(s):
            j = i%z_all
            if j>numRows-1:
                j = (numRows-1)*2-j
            result[j] += value
        res = ""
        for i in result:
            res += i
        return res






"""
最快的答案：
index代表行索引
step对索引进行修改
    如果在高速公路，step=1，保持索引增长。直至到达底端
    如果出现转折，step=-1，保持索引减小，直至出现顶端

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)
"""