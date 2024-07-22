class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_area = 0
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        def dfs(row, col):
            nonlocal max_area
            nonlocal curr_area
            visited[row][col] = True
            curr_area += 1
            max_area = max(max_area, curr_area)

            for k in range(4):
                x = row + dr[k]
                y = col + dc[k]

                if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y] and grid[x][y] == 1:
                    dfs(x, y)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    curr_area = 0
                    dfs(i, j)
        
        return max_area