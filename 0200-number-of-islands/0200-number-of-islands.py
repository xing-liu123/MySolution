class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        visited = [[False] * n for _ in range(m)]

        count = 0

        def dfs(row, col) :
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or grid[row][col] == "0":
                return
            else:
                visited[row][col] = True
                for k in range(4):
                    dfs(row + dr[k], col + dc[k])

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                   
                    count += 1
                    dfs(i, j)
        
        return count
            