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

    # XOR will returns true when only ODD numbers of conditions are TRUE.

    #         input = 2,2,1

    #         ans | nums | ans XOR nums
    #         0   | 2    | 0^2=2
    #         2.  | 2.   | 2^2=0
    #         0.  | 1.   | 0^1=1 ans=0

        nums.sort()

        for i in nums:

            ans ^= i

        return ans



# You must first know binary (base-2) system. So lets have example number 6 and number 3.
#
# These numbers converts to 0110 and 0011 in base-2 respectively.
#
# When we perform XOR on the numbers, we will perform the operations on each individual bits.
#
# Let the bits in the order of b3, b2, b1, b0. In b3 place, 0 XOR 0 will gives you 0 In b2 place,
#
# 1 XOR 0 will give you 1 In b1 place, 1 XOR 1 will give you 0 In b0 place, 0 XOR 1 will give you 1.
#
# Hence, the result is 0101 in base-2, which is 5 in base-10