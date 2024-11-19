class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            if obstacleGrid[row][0] == 1:
                break
            else:
                dp[row][0] = 1

        

        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            else:
                dp[0][col] = 1

        
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] += dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]