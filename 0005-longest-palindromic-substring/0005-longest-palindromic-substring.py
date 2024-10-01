class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        maxLen = 1
        res = s[0]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n, 1):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    elif j - i > 1:
                        dp[i][j] = dp[i + 1][j - 1]
                    
                    if dp[i][j] and j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        res = s[i: j + 1]

        return res



        