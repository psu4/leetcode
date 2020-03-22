# # 217. Contains Duplicate
#
#
#
# Share
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

# youtube: https://www.youtube.com/watch?v=xEXqi7mwPCI

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(nums) <=1:
            return false

        nums.sort()  # we sort the array first so it is faster to fund the duplicates

        for i in (0, len(nums) - 1):

            if nums[i] == nums[i + 1]:
                return True

        return False