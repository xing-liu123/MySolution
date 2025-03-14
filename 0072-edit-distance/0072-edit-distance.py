class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, min(m + 1, n + 1)):
            if word1[i - 1] == word2[i - 1]:
                dp[i][i] = dp[i - 1][i - 1]
            else:
                dp[i][i] = dp[i - 1][i - 1] + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j])
                else:
                    dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]) + 1, dp[i][j])

        return dp[m][n]
                