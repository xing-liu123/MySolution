class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)] 

        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        def dfs(x, y):
            nonlocal count
            visited[x][y] = True

            for k in range(4):
                nx, ny = x + dr[k], y + dc[k]

                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        count += 1
                    else:
                        if not visited[nx][ny]:
                            dfs(nx, ny)
                else:
                    count += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)

        return count
