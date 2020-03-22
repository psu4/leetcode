#https://www.youtube.com/watch?v=ZgEWw8lrQ5M

# 350. Intersection of Two Arrays II
# Easy
#
# Add to List
#
# Share
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution:

    def intersect(self, nums1:List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > len(nums2):

            return self.intersect(nums2,nums1)  # reverse nums2 and nums1, so that we only store the smaller array into the lookup table

        lookup = collections.defaultdict(int)  # create a lookup dictionary

        print(lookup)

        # defaultdict(<class 'int'>, {})

        for i in nums1:
            lookup[
                i] += 1  # add each element in nums1 into the lookup table, and count each element shows up how many times

        print(lookup)

        # defaultdict(<class 'int'>, {1: 2, 2: 2})

        result = []

        for i in nums2:

            if lookup[i] > 0:
                result += i,  # if i is in the lookup table, add it in the result table

                lookup[i] -= 1  # take out i from the lookup table

        return result