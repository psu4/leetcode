# 66. Plus One
# Easy
#
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

#https://www.youtube.com/watch?v=6A-DTVB9HT8


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


    # an integer 123 is represented as Input: [1,2,3]

    # so basically add 1 for the last element in the array

    # the tricky part is input=99, output=100

    # we need to reverse the digit to process the question

    # input: [1,2,3]

        for i in reversed(range(len(digits))): # range (0,3) reversed => range(3,0):

            if digits[i] == 9:  # if the first unit is 9, set it into 0

                digits[i] = 0


            else:

                digits[i] +=1

                return digits


                # now the digit is 000 for the 999 input, so we need to set the first digit =1 , and append
            # 1 more 0

        digits[0] =1

        digits.append(0)

        return digits


