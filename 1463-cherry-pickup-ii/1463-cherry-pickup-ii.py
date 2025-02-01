from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
    
        @lru_cache(None)
        def dp(i, j, k):
            if j < 0 or j >= cols or k < 0 or k >= cols:
                return float('-inf')  # If out of bounds, return negative infinity
            
            # Get cherries at current positions
            cherries = grid[i][j] + (grid[i][k] if j != k else 0)

            # If we're at the last row, return cherries
            if i == rows - 1:
                return cherries

            # Transition: Move both robots in 9 possible ways
            max_next = float('-inf')
            for dj in [-1, 0, 1]:
                for dk in [-1, 0, 1]:
                    max_next = max(max_next, dp(i+1, j+dj, k+dk))

            return cherries + max_next

        return dp(0, 0, cols-1)

