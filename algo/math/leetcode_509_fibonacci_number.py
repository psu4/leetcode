# leetcode 509 Fibonacci Number

# easy
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

class Solution:
    def fib(self, N:int) -> int:


    #         # solution 1: use golden ratio

    #         if N > 30:

    #             return print('N larger than 30')

    #         elif N<=1:

    #             return N

    #         else:

    #             golden_ratio=1.618034

    #             return round((golden_ratio**N - (1-golden_ratio)**N)/math.sqrt(5))

    #         # space O(1), TIME complexity O(1)



    # solution 2: recursion


        if N > 30:

            return
            print('N larger than 30')

        elif N <= 1:

            return N

        return self.fib(N - 1) + self.fib(N - 2)

        # time: 2^N  space: N