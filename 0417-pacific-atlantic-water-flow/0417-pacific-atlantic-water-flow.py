class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        def dfs(row, col, visited):
            visited[row][col] = True

            for k in range(4):
                x, y = row + dr[k], col + dc[k]

                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if heights[x][y] >= heights[row][col]:
                        visited[x][y] = True
                        dfs(x, y, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)
        
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        res = [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
        
        return res

    

        