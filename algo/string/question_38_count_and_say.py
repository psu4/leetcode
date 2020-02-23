# leetcode 38

# good solution: https://www.youtube.com/watch?v=zOOKD2OBIUY
#
# The count-and-say sequence is the sequence of integers with the first five terms as following:

#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a string.


class Solution:
    def countAndSay(self, n: int) -> str:

    # basic logic: get the next sequence from the current sequence

    # 1

    # 11

    # 21

    # 1211

    seq = "1"  # the first seq must be 1

    for i in range(n - 1):  # because it starts with 0

        seq = self.getNext(seq)

    return seq


def getNext(self, seq):
    i = 0

    next_seq = ""

    while i < len(seq):

        count = 1  # we refresh the count every time

        while i < len(seq) - 1 and seq[i] == seq[
                    i + 1]:  # if the number is the same as the next one in the same sequence, continue

            count = count + 1

            i = i + 1

        next_seq = next_seq + str(count) + seq[i]

        i = i + 1

    return next_seq


    # in round 1, seq=1;

    # next seq= str(1) + seq[0] = 11

    #    def getNext(self, seq):

    #                 i = 0

    #         next_seq = ""

    #         while i < len(seq):   # i < 1

    #             count=1 # we refresh the count every time

    #             while i < len(seq)-1 and seq[i]==seq[i+1]: #if the number is the same as the next one in the same sequence

    #                 count= count+1

    #                 i=i+1

    #             next_seq= next_seq + str(count) + seq[i]  # return 11

    #             i = i+1

    #         return next_seq



    #    in round 2: seq=2

    #    def getNext(self, seq):

    #                 i = 0

    #         next_seq = ""         # 11

    #         while i < len(seq):   # i < 2

    #             count=1 # we refresh the count every time

    #             while i < len(seq)-1 and seq[i]==seq[i+1]:  # i < 1 and seq[1]==seq[2]


    #                 count= count+1

    #                 i=i+1

    #             next_seq= next_seq + str(count) + seq[i]  # return 21

    #             i = i+1        i=1

    #         return next_seq