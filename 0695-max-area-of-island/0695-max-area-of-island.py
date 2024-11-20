class Solution:
    
    def __init__(self):
        self.res = 0
        self.currMax = 0   

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        def dfs(x, y):
            grid[x][y] = 0
            self.currMax += 1

            for k in range(4):
                nx, ny = x + dr[k], y + dc[k]

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    self.res = max(self.res, self.currMax)
                    self.currMax = 0

        return self.res