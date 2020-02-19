# Example 1:
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.




class Solution:

    # time complexity: O(N)

    # space complexity: O(1)

    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        # use 2 pointers to solve this problem  a=0

        b=len(s)-1

        while a < b:

            temp=s[a]

            s[a]=s[b]

            s[b]=temp

            a=a+1

            b=b-1
