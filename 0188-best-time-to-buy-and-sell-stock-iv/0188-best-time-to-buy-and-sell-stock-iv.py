class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        dp = [[0]*(2 * k) for _ in range(len(prices))]

        for i in range(k):
            dp[0][2 * i] = -prices[0]
        
        for i in range(1, len(prices)):
            for j in range(2 * k):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], -prices[i])
                elif j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        
        return dp[-1][-1]