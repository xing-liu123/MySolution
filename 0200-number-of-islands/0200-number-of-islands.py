class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1] # up, down, right, left
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            grid[row][col] = "0"

            for k in range(4):
                nr, nc = row + dr[k], col + dc[k]

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                    dfs(nr, nc)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count