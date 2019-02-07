"""
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        if 0 in d and d[0] > 2:
            rst = [[0, 0, 0]]
        else:
            rst = []

        pos = [p for p in d if p > 0]
        neg = [n for n in d if n < 0]

        # 如果出现相等的情况
        # 如果出现不相等的情况，为避免出现重复，如果是正数，取较大，如果是负数，取较小
        # 特殊情况出现0时，不会出现两种情形的交换，因此拎出来
        for p in pos:
            for n in neg:
                inverse = -(p + n)
                if inverse in d:
                    if inverse in (p, n) and d[inverse] > 1:
                        rst.append([n, inverse, p])
                    if inverse < n or inverse > p or inverse == 0:
                        rst.append([n, inverse, p])

        return rst