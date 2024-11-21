class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        currArea = 0
        maxArea = 0

        m, n = len(grid), len(grid[0])
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        def dfs(x, y, marker):
            nonlocal currArea
            currArea += 1
            grid[x][y] = marker

            for k in range(4):
                nx, ny = x + dr[k], y + dc[k]

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny, marker)

        marker = 2
        areas = {}
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    currArea = 0
                    dfs(i, j, marker)
                    areas[marker] = currArea
                    marker += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    if i > 0 and grid[i - 1][j] > 0:
                        neighbors.add(grid[i - 1][j])

                    if i < m - 1 and grid[i + 1][j] > 0:
                        neighbors.add(grid[i + 1][j])

                    if j > 0 and grid[i][j - 1] > 0:
                        neighbors.add(grid[i][j - 1])

                    if j < n - 1 and grid[i][j + 1] > 0:
                        neighbors.add(grid[i][j + 1])

                    area = 1

                    for nei in neighbors:
                        area += areas.get(nei, 0)

                    maxArea = max(maxArea, area)
                    

        return maxArea if maxArea > 0 else m * n