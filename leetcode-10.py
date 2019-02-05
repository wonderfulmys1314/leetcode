"""
    给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

    '.' 匹配任意单个字符。
    '*' 匹配零个或多个前面的元素。
    匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

    说明:

    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
    示例 1:

    输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。
    示例 2:

    输入:
    s = "aa"
    p = "a*"
    输出: true
    解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
    示例 3:

    输入:
    s = "ab"
    p = ".*"
    输出: true
    解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
    示例 4:

    输入:
    s = "aab"
    p = "c*a*b"
    输出: true
    解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
    示例 5:

    输入:
    s = "mississippi"
    p = "mis*is*p*."
    输出: false
"""


"""
    没有头绪，开始直接找的最快的人的方法
    后来看了别人的想法，参考写出了动态规划的方法
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn = len(s) + 1
        pn = len(p) + 1
        d = [[False for i in range(pn)] for j in range(sn)]
        d[0][0] = True

        for i in range(sn):
            for j in range(1, pn):
                if p[j - 1] != "*":
                    d[i][j] = i > 0 and d[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == ".")
                else:
                    d[i][j] = j > 1 and (
                    (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == ".") and d[i - 1][j]) or d[i][j - 2])

        return d[sn - 1][pn - 1]


"""
我觉得这里之所以能够简化主要在于：
模式中每次出现新的，就需要对b[j]进行更新
情形可分为：
    如果当前是“.”,后一位是“*”
    如果当前不是”.”,后一位是“*”
    如果后一位不是”*“

class Solution:
    def isMatch(self, s, p):
        sn, pn = len(s), len(p)
        b = [False] * (sn + 1)
        b[0] = True
        i = 0
        while i < pn:
            # 取当前值
            c = p[i]
            i += 1
            # 后一位值如果为*
            if i < pn and p[i] == "*":
                # 如果当前值为"."
                if c == ".":
                    # 遍历字符串
                    for j in range(sn):
                        if b[j]:
                            for k in range(j + 1, sn + 1):
                                b[k] = True
                            break
                else:
                    for j in range(sn):
                        if s[j] == c:
                            b[j + 1] = b[j] or b[j + 1]

                i += 1
            # 如果不为*的话
            else:
                for j in reversed(range(sn)):
                    b[j + 1] = b[j] and (s[j] == c or c == ".")
                b[0] = False
        return b[-1]
"""