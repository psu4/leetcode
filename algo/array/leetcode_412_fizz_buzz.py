# 412. Fizz Buzz
# Easy
#
# 767
#
# 1057
#
# Add to List
#
# Share
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution:
    def fizzBuzz(self, n:int) -> List[str]:

    return_list = []

    for i in range(1, n + 1):

        if i % 15 == 0:

            return_list.append('FizzBuzz')

        elif i % 3 == 0:

            return_list.append('Fizz')

        elif i % 5 == 0:

            return_list.append('Buzz')

        else:

            i_str = str(i)

            return_list.append(i_str)

    return return_list