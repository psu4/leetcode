# 204. Count Primes
# Easy
#
# 1688
#
# 539
#
# Add to List
#
# Share
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Accepted
# 324,159
# Submissions
# 1,051,501

class Solution:
    def countPrimes(self, n:int) -> int:

    # the goal here is to generate a list of numbers 0-N

    # [0,1,2,3,4,5,6]

    # https://www.youtube.com/watch?v=UGeCe5WQNVg

        if n <= 1:

            return 0

        nums = [None] * n

        # [False, False, 2,3,4,5,6] put prime number as false
    
        nums[0] = False

        nums[1] = False

        for i in range(n):

            #             print(i)

            #             print(nums[i])

            if nums[i] == None:  # if i is the next prime number

                nums[i] = True  # set i=True # [False, False, True ,3,4,5,6]

                for j in range(i + i, n, i):  # then set all the numbers that can be divided by this primve number as False

                    # print(j)
                    nums[j] = False  # [False, False, True ,3, False, 5, False]

        return sum(nums)



