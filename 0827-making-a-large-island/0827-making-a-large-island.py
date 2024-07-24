class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        area = 0
        m, n = len(grid), len(grid[0])
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        def dfs(row, col, visited):
            nonlocal area
            nonlocal largest
            area += 1
            visited[row][col] = True

            largest = max(largest, area)

            for k in range(4):
                x, y = row + dr[k], col + dc[k]

                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == 1:
                    dfs(x, y, visited)

    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 0
                    visited = [[False] * n for _ in range(m)]
                    dfs(i, j, visited)

        return largest if area != 0 else m * n



    