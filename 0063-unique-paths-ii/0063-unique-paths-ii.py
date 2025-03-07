class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1

        for row in range(m):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] += dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]