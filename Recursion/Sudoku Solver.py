# https://leetcode.com/problems/sudoku-solver
# hard problem
# Actual problem: Place numbers(1 to 9) at 'E' places
# Sub-problem: Place numbers(1 to 9) at 1,2,....E-1,E places

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Solution.helper(self, board)
        print("updated board : ", board)

    def helper(self, board):
        # iterate through each box
        for i in range(9):
            for j in range(9):
                # if box is empty
                if board[i][j] == ".":
                    # for each number validate if number is valid and if yes add to box
                    for c in range(1, 10):
                        if Solution.is_valid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            # if solution found no need to backtrack return true
                            if Solution.helper(self, board):
                                return True
                            board[i][j] = "."
                    # can't place any of the 9 digits at i, j and number added in the box is incorrect so return false
                    return False
        # got the answer and box is filled so return true
        return True

    @staticmethod
    def is_valid(board, row, col, c):

        for i in range(9):
            # check row
            if board[i][col] == c:
                return False
            # check column
            if board[row][i] == c:
                return False
            # check 3x3 board
            x = int(row / 3)
            y = int(col / 3)
            if (board[3 * x + int(i / 3)][3 * y + int(i % 3)]) == c:
                return False
        return True


if __name__ == '__main__':
    nums = [["5", "3", ".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print("board : ", nums)
    s = Solution()
    s.solveSudoku(nums)
