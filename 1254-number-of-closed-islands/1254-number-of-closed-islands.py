class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        def dfs(x, y):
            grid[x][y] = 1

            for k in range(4):
                nx, ny = x + dr[k], y + dc[k]

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                    dfs(nx, ny)

        
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)

            if grid[i][n - 1] == 0:
                dfs(i, n - 1)

        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)

            if grid[m - 1][j] == 0:
                dfs(m - 1, j)

        count = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1

        return count