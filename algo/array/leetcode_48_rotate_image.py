# 48. Rotate Image
# Medium
#
# Add to List
#
# Share
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # Michelle's solution is a bit complicated

    # https://www.youtube.com/watch?v=OlO_bzYidFM

    # easier solution: transpose and then reverse

    # time complexity= N^2, space complexity=1


        n = len(matrix)

        for i in range(0, n):

            for j in range(i, n):
                
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse matrix per row

        for i in range(n):
            matrix[i].reverse()

