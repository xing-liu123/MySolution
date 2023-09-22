class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        dp = [[0] * 2 for _ in range(n)] 

        dp[0][0] = -prices[0] - fee
        
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        return max(dp[n - 1][0], dp[n - 1][1])