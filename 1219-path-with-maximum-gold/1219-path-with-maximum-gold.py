class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        visited = [[False] * n for _ in range(m)]

        def backtracking(row, col, curr_gold):
            nonlocal max_gold

            max_gold = max(max_gold, curr_gold)

            for k in range(4):
                x = row + dr[k]
                y = col + dc[k]

                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] != 0:
                    visited[x][y] = True
                    backtracking(x, y, curr_gold + grid[x][y])
                    visited[x][y] = False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    backtracking(i, j, grid[i][j])
                    visited[i][j] = False
        return max_gold



