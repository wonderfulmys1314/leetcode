"""
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

    例如，给出 n = 3，生成结果为：

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
"""

"""
    这道题知很好
    主要是要理解递归、回溯、规划
    参考官方题解
"""


"""
    方法一：
    走出else流程便结束
    但是过程中会不断的深入使得A不断增加
    到达A的长度等于2n时，便开始回溯尝试
    其实就是回溯法的递归
    递归怎么写真的需要学习呀，明确递归操作呀
"""
class SolutionOne(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        # 验证是否满足平衡
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans


"""
    方法二：
    还是使用递归完成回溯
    这里最大的区别是在递归的过程中保持平衡
    如果出现不够，就补
    如果出现不平衡，也补，最终达到满额
"""


class SolutionTwo(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

"""
    方法三：
    主要是以一对括号为单位进行添加
    此时可分为两种情况
        一种在括号内部
        一种在括号外部
"""

class SolutionThree(object):
    def generateParenthesis(self, N):
        if N == 0:
            return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans