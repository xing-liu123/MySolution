class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.'* n for _ in range(n)]
        res = []
        
        def backtracking(row):
            if row == n:
                res.append(board.copy())
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                    backtracking(row + 1)
                    board[row] = board[row][:col] + '.' + board[row][col + 1:]
            
        
        def isValid(row, col) -> bool:
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            i, j = row - 1, col - 1
            
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                
                i -= 1
                j -= 1
                
            i, j = row - 1, col + 1
            
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                
                i -= 1
                j += 1
            
            return True
        
        backtracking(0)
            
        return res

            