# 1. Two Sum
# Easy
#
# Add to List
#
# Share
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]. 


# nums = [2, 7, 11, 15]
# target = int(9)

# class Solution:

#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         h = {}
#         for i, num in enumerate(nums):
#             n = target - num
#             if n not in h:
#                 h[num] = i
#             else:
#                 return [h[n], i]


# d=Solution().twoSum

# print(d(nums,target))

# https://www.youtube.com/watch?v=OTtbG8lNNW8

nums = [2, 7, 11, 15]
target = int(9)


class Solution(object):
    def twoSum(self, nums, target):

        d = {}

        for i in range(len(nums)):

            if target - nums[i] not in d:  # 9-2=7  | 9-7=2

                d[nums[i]] = i  # 2:0

            else:

                return [d[target - nums[i]], i]



