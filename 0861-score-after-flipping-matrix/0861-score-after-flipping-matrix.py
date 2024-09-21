import numpy as np
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = np.array(grid)

        oneInCol = np.sum(grid, axis = 0)

        for row in range(m):
            if grid[row][0] == 0:
                oneInCol[0] += 1
                for col in range(1, n):
                    if grid[row][col] == 0:
                        oneInCol[col] += 1
                    else:
                        oneInCol[col] -= 1

        oneInCol[0] = m

        exp = n - 1

        res = 0

        for base in oneInCol:
            res += max(base, m - base) * 2 ** (exp)
            exp -= 1
        
        return res

        