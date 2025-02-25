class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1] # up, down, right, left
        m, n = len(grid), len(grid[0])

        count = 0

        def dfs(currRow, currCol):
            grid[currRow][currCol] = "0"

            for k in range(4):
                newRow, newCol = currRow + dr[k], currCol + dc[k]

                if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == "1":
                    dfs(newRow, newCol)

        for i in range(m):
            for j in range(n):
                # a new island is found
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count