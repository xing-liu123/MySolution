class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i + 1) for i in range(query_row + 2)]

        dp[0][0] = poured

        for i in range(query_row + 1):
            for j in range(i + 1):
                excess = 0
                if dp[i][j] > 1:
                    excess = dp[i][j] - 1
                    dp[i][j] = 1
                
                dp[i + 1][j] += excess / 2
                dp[i + 1][j + 1] += excess / 2
        
        return min(dp[query_row][query_glass], 1)
                    