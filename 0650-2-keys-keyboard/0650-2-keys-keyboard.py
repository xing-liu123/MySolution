class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)

        dp[1] = 0

        for i in range(1, n + 1):
            paste = 1
            for j in range(2 * i, n + 1, i):
                dp[j] = min(dp[j], dp[i] + 1 + paste)
                paste += 1
        
        return dp[n]
