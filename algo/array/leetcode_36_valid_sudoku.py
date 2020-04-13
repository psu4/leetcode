# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# A partially filled sudoku which is valid.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Example 1:
#
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:
#
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.


# video: https://www.youtube.com/watch?v=1FUFPovVhZs

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        return self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board)

# input:
# >>> l=["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."]

# >>> l=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."]]
# >>> print(l)
# [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.']]
# >>> print(type(l))
# <type 'list'>
# >>> zip(*l)
# [('5', '6'), ('3', '.'), ('.', '.'), ('.', '1'), ('7', '9'), ('.', '5'), ('.', '.'), ('.', '.'), ('.', '.')]

    def is_row_valid(self, board):
        for row in board:

            if not self.is_unit_valid(row):
                return False

        return True


    def is_col_valid(self, board):
        for col in zip(*board):

            if not self.is_unit_valid(col):
                return False

        return True


    def is_square_valid(self, board):
        for i in (0, 3, 6):

            for j in (0, 3, 6):

                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]

                print(square)

                if not self.is_unit_valid(square):
                    return False

        return True


    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']  # we only want to keep the numbers in the input

        # if the length of numbers and the unique numbers length are the same, return true

        return len(set(unit)) == len(unit)



