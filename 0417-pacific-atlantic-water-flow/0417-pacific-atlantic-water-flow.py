class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]

        for i in range(m):
            pacific[i][0] = True
        
        for j in range(n):
            pacific[0][j] = True
        
        atlantic = [[False] * n for _ in range(m)]

        for i in range(m):
            atlantic[i][-1] = True
        
        for j in range(n):
            atlantic[-1][j] = True

        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            if not visited[i][0]:
                self.dfs(i, 0, pacific, dr, dc, heights, visited)
        
        for j in range(n):
            if not visited[0][j]:
                self.dfs(0, j, pacific, dr, dc, heights, visited)

        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            if not visited[i][n - 1]:
                self.dfs(i, n - 1, atlantic, dr, dc, heights, visited)

        
        for j in range(n):
            if not visited[m - 1][j]:
                self.dfs(m - 1, j, atlantic, dr, dc, heights, visited)

        res = []

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        
        return res

    def dfs(self, row, col, grid, dr, dc, heights, visited):
        visited[row][col] = True
        for k in range(4):
            x, y = row + dr[k], col + dc[k]

            if x >= 0 and x < len(heights) and y >= 0 and y < len(heights[0]) and not visited[x][y]:
                if heights[x][y] >= heights[row][col]:
                    grid[x][y] = True
                    self.dfs(x, y, grid, dr, dc, heights, visited)

        