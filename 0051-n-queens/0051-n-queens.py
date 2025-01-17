class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def solve(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = "Q"
                    solve(row + 1)
                    board[row][col] = "."

        def isValid(row, col):
            # check upper
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # check upper-left

            i, j = row - 1, col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        solve(0)

        return res
        
