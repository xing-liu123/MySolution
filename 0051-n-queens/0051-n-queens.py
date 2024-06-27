class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = ['.' * n for _ in range(n)]
        
        res = []
        
        def backtracking(row):
            if row == n:
                res.append(path.copy())
                return
            
            for j in range(0, n):
                if isValid(row, j):
                    path[row] = path[row][:j] + 'Q' + path[row][j + 1:]
                    backtracking(row + 1)
                    path[row] = path[row][:j] + '.' + path[row][j + 1:]
                
        def isValid(row, col):
            for i in range(row - 1, -1, -1):
                if path[i][col] == 'Q':
                    return False

            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if path[i][j] == 'Q':
                    return False
                j -= 1
                i -= 1
            
            i = row - 1
            j = col + 1
            
            while i >= 0 and j < n:
                if path[i][j] == 'Q':
                    return False
                j += 1
                i -= 1

            return True
        
        backtracking(0)
        
        return res