# 88. Merge Sorted Array
# easy
# https://www.youtube.com/watch?v=ANUDq_2Bs04

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

class Solution:

    def merge(self, nums1:List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # solution 1: merge and sort

        # space compexlity=1

        # time complexity=O((n+m)log(n+m))

        nums1[:] = sorted(nums1[:m] + nums2)

        #         return nums1[:]

        # solution 2: 2 pointers

        # Time complexity : O(n+m)
        # Space complexity : O(1)

        # if the last element in nums2 is larger than the last non-zero digit in nums1

        # put the last element in nums2 into the end of nums1

        while m > 0 and n > 0:

            if nums2[n - 1] > nums1[m - 1]:

                nums1[m + n - 1] = nums2[n - 1]

                n = n - 1

                # if the last element in nums2 is smaller than the last non-zero digit in nums1

            # put the last non-zero digit in nums1 into the end of nums1, and last element in nums2

            # put into the last non-zero digit in nums1's position

            else:

                nums1[m + n - 1], nums1[m - 1] = nums1[m - 1], nums1[m + n - 1]

                m = m - 1

        if m == 0 and n > 0:  # if nums2 is longer than nums1

            nums1[:n] = nums2[:n]