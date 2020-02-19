
# easy

#Given two strings s and t , write a function to determine if t is an anagram of s.

# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Input: s = "rat", t = "car"
# Output: false

# solution 1:  use the Counter function
# from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         a=Counter(s)
#         b=Counter(t)

#         if a == b:

#             return True

#         else:

#             return False


# good video explanation: https://www.youtube.com/watch?v=IRN1VcA8CGc&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-&index=138&t=0s

# Time complexity: O(N)

# space complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):

        return False

    dict = {}

    for char in s:  # count how many each char in s
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in t:
        if char not in dict:
            return False
        else:  # if a char exists in both s and t, reduce it
            dict[char] -= 1

    for val in dict.values():

        if val != 0:  # if val != 0 meaning the 2 words are not anagram

            return False

    return True



