"""
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

    注意：

    答案中不可以包含重复的四元组。

    示例：

    给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

    满足要求的四元组集合为：
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]

"""

"""
    虽然我自己的方法也可以，但是这个目前效率最高的方法主要是在细节方面做得比较好
    主要受提出可能出现的重复情况
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)
        result = []

        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                start = j + 1
                end = length - 1
                if nums[i] + nums[j] + nums[start] + nums[start + 1] > target:
                    break
                elif nums[i] + nums[j] + nums[end - 1] + nums[end] < target:
                    pass
                else:
                    while start < end:
                        if nums[i] + nums[j] + nums[start] + nums[end] < target:
                            start += 1
                        elif nums[i] + nums[j] + nums[start] + nums[end] > target:
                            end -= 1
                        else:
                            if [nums[i], nums[j], nums[start], nums[end]] not in result:
                                result.append([nums[i], nums[j], nums[start], nums[end]])
                            start += 1
                            end -= 1
        return result


"""
class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        # 这种求和为了减少步骤首先是排序比较  哎哎哎
        a = nums[:4]
        if sum(nums[:4]) > target:
            return res
        for index, num in enumerate(nums[:-3]):
            target1 = target - num
            if sum(nums[index: index + 4]) > target:
                break
                # 下面的条件是最后的三个数比target1还小就是在target1固定的情况下达不到目标了
                # 或者是我现在的数和我上一次的数相同  确实 这种情况下不进行下一个循环就会重复
                # 记住 这个条件总的就是 要么达不到 要么会重复所以跳过
            elif sum(nums[-3:]) < target1 or (index > 0 and num == nums[index - 1]):
                continue
                # 在固定第一个后第二个数进行循环 因为是四个数所以截止到倒数第三个
            for j in range(index + 1, len(nums) - 2):
                target2 = target1 - nums[j]
                # 同样的道理 两种情况剔除
                if nums[j + 1] + nums[j + 2] > target2:
                    break
                elif nums[-2] + nums[-1] < target2 or (j > index + 1 and nums[j] == nums[j - 1]):
                    continue
                    # 再把特殊情况剔除后达到我们最后两个数的和等于目标  用双指针法  但为什么这么写会快很多啊 不是很懂 ：（
                l, r = j + 1, len(nums) - 1
                while l < r:
                    temp = nums[l] + nums[r]
                    if temp > target2:
                        r -= 1
                    elif temp < target2:
                        l += 1
                    else:
                        res.append([num, nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        #相等之后确实两面都要移  不然会重复 因为这两个数相等的结果都有了
                        l += 1
                        r -= 1
        return res

"""