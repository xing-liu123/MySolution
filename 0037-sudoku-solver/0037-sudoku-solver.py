class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n = len(board)

        def isValid(row: int, col: int, val: str) -> bool:
            # Check row
            for j in range(n):
                if board[row][j] == val:
                    return False

            # Check column
            for i in range(n):
                if board[i][col] == val:
                    return False

            # Check square
            for i in range(row // 3 * 3, row // 3 * 3 + 3):
                for j in range(col // 3 * 3, col // 3 * 3 + 3):
                    if board[i][j] == val:
                        return False

            return True

        def solve():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == ".":
                        for val in range(1, 10):
                            if isValid(i, j, str(val)):
                                board[i][j] = str(val)
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        solve()