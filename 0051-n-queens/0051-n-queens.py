class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ['.' * n for _ in range(n)]

        def backtrack(row: int):
            if row == n:
                res.append(copy.copy(board))
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row] = board[row][0 : col] + 'Q' + board[row][col + 1:]
                    backtrack(row + 1)
                    board[row] = board[row][0 : col] + '.' + board[row][col + 1:]
        
        def isValid(row: int, col: int) -> bool:
            for i in range(0, row):
                if board[i][col] == 'Q':
                    return False
            
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        backtrack(0)

        return res