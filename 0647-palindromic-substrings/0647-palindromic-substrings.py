class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * (n) for _ in range(n)]

        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if i + 1 == j or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1

        return count                    
                        