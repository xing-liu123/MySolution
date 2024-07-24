class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        visited = [[False] * n for _ in range(m)]
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        count = 0

        def isSubIsland(row, col) -> bool:
            visited[row][col] = True

            isSub = True

            if grid1[row][col] == 0:
                isSub = False
            
            for k in range(4):
                x, y = row + dr[k], col + dc[k]

                if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1 and not visited[x][y]:
                    if not isSubIsland(x, y):
                        isSub = False
                        
            return isSub

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if isSubIsland(i, j):
                        print("end")
                        count += 1
        
        return count