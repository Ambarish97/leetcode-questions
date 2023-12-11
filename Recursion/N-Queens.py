class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [None] * n
        s = ["."] * n
        ans = []
        for i in range(n):
            board[i] = s
        Solution.helper(self, n, board, 0, ans)
        return ans

    def helper(self, n, board, col, ans):
        if col == n:
            copy = ["".join(row) for row in board]
            ans.append(copy)
            print("ans", ans)
            return

        for row in range(0, n):
            if Solution.is_valid(self, board, row, col, n):
                board[row][col] = 'Q'
                Solution.helper(self, n, board, col + 1, ans)
                board[row][col] = "."

    def is_valid(self, board, row, col, n):
        # check horizontally
        for j in range(col):
            if board[row][j] == 'Q':
                return False

        # check diagonal left top
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # check diagonal left bottom
        r = row + 1
        c = col - 1
        while r <= n and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1
        return True

if __name__ == '__main__':
    nums = 4
    s = Solution()
    no = s.solveNQueens(nums)
    print("Output : ", no)