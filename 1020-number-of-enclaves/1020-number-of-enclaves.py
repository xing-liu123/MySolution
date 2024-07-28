class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        n, m = len(grid), len(grid[0])

        def dfs(row, col):
            
            grid[row][col] = 0

            for k in range(4):
                x, y = row + dr[k], col + dc[k]

                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                    dfs(x, y)

        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
            
            if grid[i][m - 1] == 1:
                dfs(i, m - 1)

        for i in range(m):
            if grid[0][i] == 1:
                dfs(0, i)
            
            if grid[n - 1][i] == 1:
                dfs(n - 1, i)

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
            
        return count