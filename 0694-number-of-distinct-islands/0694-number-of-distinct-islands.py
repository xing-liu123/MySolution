class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]
        m, n = len(grid), len(grid[0])


        def dfs(row, col, direction, move):
            grid[row][col] = 0
            move.append(direction)
            for k in range(4):
                next_row, next_col = row + dr[k], col + dc[k]

                if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == 1:
                    
                    dfs(next_row, next_col, k, move)
        
            move.append("b")
        
        moves_set = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    move = []
                    dfs(i, j, "s", move)

                    moves_set.add(tuple(move))

        

        return len(moves_set)
