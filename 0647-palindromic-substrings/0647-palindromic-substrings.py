class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]

        count = 0
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        

        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if i == j - 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                elif j - i > 1:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
        
        return count