class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for i in  range(len(prices))]
        
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        
        return max(dp[len(prices) - 1][0], dp[len(prices) - 1][1])

