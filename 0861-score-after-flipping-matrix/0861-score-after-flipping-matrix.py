import numpy as np
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for row in range(m):
            if grid[row][0] == 0:
                
                for col in range(n):
                    grid[row][col] ^= 1

        res = 0

        for col in range(n):
            ones = sum(grid[row][col] for row in range(m))
            res += max(ones, m - ones) * (1 << (n - col - 1))

        
        return res

        