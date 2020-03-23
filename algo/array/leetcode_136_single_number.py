#
# 136. Single Number
# Easy

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

# XOR: https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do

# XOR: https://stackoverflow.com/questions/60797352/what-does-the-operator-mean-in-python

# XOR: https://stackoverflow.com/questions/60797352/what-does-the-operator-mean-in-python


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

    # https://www.youtube.com/watch?v=zAXk82X7hhU

    # use XOR to solve this problem

    #         input = 2,2,1

    #         ans | nums | XOR
    #         0   | 2    | 0^2=2
    #         2.  | 2.   | 2^2=0
    #         0.  | 1.   | 0^1=1 ans=0

        nums.sort()

        for i in nums:

            ans ^= i

        return ans