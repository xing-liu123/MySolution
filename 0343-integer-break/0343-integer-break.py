class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 1

        for i in range(n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        return dp[n]
    