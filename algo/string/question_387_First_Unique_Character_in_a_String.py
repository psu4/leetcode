# 387. First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

class Solution:

    def firstUniqChar(self, s: str) -> int:

    # good video explanation

    # https://www.youtube.com/watch?v=Sh2QlIKY0GU

    # solution: create a dictionary and store the count info there

    # then return the indexes where the count==1

    # time complexity=O(N)

    # space complexity=O(N)

    dict = {}

    for i in range(len(s)):

        if s[i] not in dict:

            dict[s[i]] = 1

        elif s[i] in dict:

            dict[s[i]] += 1

    for i in range(len(s)):

        if dict[s[i]] == 1:
            return i

    return -1

