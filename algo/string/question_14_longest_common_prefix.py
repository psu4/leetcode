# 14. Longest Common Prefix
#


# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

    # https://www.youtube.com/watch?v=cGQez9SiScw

    # the algo here is to take the first element in the list and compare it to the other elements

    # if the prefixes are different, then reduce the word from the end

    # flower vs flow => reduce r from flower

    # flowe vs flow => reduce e from flowe

    # flow vs flow => the same. stop

    if len(strs) == 0: return ""

    prefix = strs[0]

    for i in range(len(prefix)):

        for string in strs[1:]:  # strs[1:]= all the elements in the list except the prefix

            if i >= len(string) or string[i] != prefix[i]:

                # if the prefix is longer than the compared word,
                # or the ith element in the prefix is not equal to the ith element in the compared word

                return prefix[:i]

    return strs[0]  # if the input is [""] which is an empty string, return the empty string
