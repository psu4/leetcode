# easy

# Given an array nums, write a function to move all 0's to the end of it while maintaining
#
# the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    #https: // www.youtube.com / watch?v = VSeVT - oKZE4
    #  [0,1,0,3,12]

    #         pos | i  | nums[i]

    #         0   | 0  | 0

    #         1.    1    1

        pos = 0

        for i in range(len(nums)):  # if the numbers are not 0, put them to the front with the same order

            if nums[i] != 0:
                nums[pos] = nums[i]

                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0

        return nums