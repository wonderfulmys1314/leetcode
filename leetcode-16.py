"""
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

"""
    别人的方法比我优秀的地方在于提前截止
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, n = [], len(nums)
        for index, num in enumerate(nums[:-2]):
            left, right = index + 1, n - 1
            min_ = num + nums[left] + nums[left + 1]
            if min_ > target:
                res.append(min_)
                break
            elif num + nums[right] + nums[right - 1] < target:
                res.append(num + nums[right] + nums[right - 1])
            else:
                while left < right:
                    temp = num + nums[left] + nums[right]
                    res.append(temp)
                    if temp > target:
                        right -= 1
                    elif temp < target:
                        left += 1
                    else:
                        return target
        res.sort(key=lambda x: abs(x - target))
        return res[0]