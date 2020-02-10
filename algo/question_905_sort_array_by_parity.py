# 905. Sort Array By Parity
#
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
# Note:
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

# class ListNode:
#     def __init__(self,x):
#         self.val= x
#         self.next= None

# quick sort: https://www.youtube.com/watch?v=PgBzjlCcFvc

class Solution:
    def sortArrayByParity(self, A:
        List[int]

    ) -> List[int]:

    # we need 2 pointers to track both even and odd numbers

    # (1) 3, 1, 2, 4
    # (2) 4, 1, 2, 3
    # (3) 4, 2, 1, 3

    i, j = 0, len(A) - 1

    while i < j:

        if A[i] % 2 > A[j] % 2:  # then swamp the 2

            A[i], A[j] = A[j], A[i]

        if A[i] % 2 == 0:
            i = i + 1
        if A[j] % 2 == 0:
            j = j - 1
    return A


# Complexity
# Analysis

# Time Complexity: O(N), where N is the length of A. Each step of the while loop makes j-i decrease by at least one. (Note that while quicksort is O(Nlog N) normally, this is O(N) because we only need one pass to sort the elements.)

# Space Complexity: O(1) in additional space complexity.


# other solution:

# https://leetcode.com/problems/sort-an-array/discuss/277127/7-line-quicksort-to-write-in-interviews-python