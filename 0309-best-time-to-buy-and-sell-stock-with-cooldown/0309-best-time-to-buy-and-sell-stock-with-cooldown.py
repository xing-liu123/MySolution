class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
            
        dp = [[0] * 2 for _ in range(n)]

        dp[0][1] = -prices[0]
        dp[1][0] = max(0, prices[1] - prices[0])
        dp[1][1] = max(-prices[0], -prices[1])

        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return max(dp[-1])
            