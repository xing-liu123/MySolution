class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n] == m
        # i = 0
        # j = 0

        # while i < m and j < n:
        #     if s[i] == t[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        
        # return i == m
