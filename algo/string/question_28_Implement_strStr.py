# 28. Implement strStr()
# Easy
#
# 1282
#
# 1689
#
# Add to List
#
# Share
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1



# https://www.youtube.com/watch?v=62lXzTIHTiI

class Solution:
    def strStr(self, haystack:str, needle: str) -> int:

    for i in range(len(haystack) - len(needle) + 1):

        if haystack[i: i + len(needle)] == needle:
            return i

    return -1