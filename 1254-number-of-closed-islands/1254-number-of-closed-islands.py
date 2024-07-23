class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        res = 0

        def isClosed(row, col) -> bool:
            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            if grid[row][col] == 1:
                return True

            grid[row][col] = 1    
            
            closed = True

            for k in range(4):
                x = row + dr[k]
                y = col + dc[k]
            
                if not isClosed(x, y):
                    closed = False
            
            return closed
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and isClosed(i, j):
                    res += 1
        
        return res