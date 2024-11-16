class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def solve(currRow: int):
            if currRow == n:
                res.append([''.join(row) for row in board])
                return

            for col in range(n):
                if isValid(currRow, col):
                    board[currRow][col] = "Q"
                    solve(currRow + 1)
                    board[currRow][col] = "."

        def isValid(row: int, col: int) -> bool:
            # Check this col
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper left
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper right
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        solve(0)
        return res