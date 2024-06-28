class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    
                    for k in range(1, 10):
                        val = str(k)
                        if isValid(i, j, val):
                            board[i][j] = val
                            if solve():
                                return True
                            board[i][j] = '.'
                    
                    return False
            
            return True
        
        def isValid(row, col, val) -> bool:
            for i in range(9):
                if board[i][col] == val:
                    return False
            
            for j in range(9):
                if board[row][j] == val:
                    return False
            
            for i in range(row // 3 * 3, row // 3 * 3 + 3):
                for j in range(col // 3 * 3, col // 3 * 3 + 3):
                    if board[i][j] == val:
                        return False
            
            return True
        
        solve()