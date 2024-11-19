class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0

        for i in range(int(math.sqrt(n)) + 1):
            square_i = i * i
            for j in range(square_i, n + 1):
                dp[j] = min(dp[j], dp[j - square_i] + 1)
        
        return dp[n]