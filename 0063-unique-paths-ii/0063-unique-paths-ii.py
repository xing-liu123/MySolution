class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(1, m):
            if dp[i - 1][0] != 0 and obstacleGrid[i][0] != 1:
                dp[i][0] = 1

        for j in range(1, n):
            if dp[0][j - 1] != 0 and obstacleGrid[0][j] != 1:
                dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]