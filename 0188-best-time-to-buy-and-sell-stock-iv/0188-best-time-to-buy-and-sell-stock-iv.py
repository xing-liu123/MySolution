class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2 * k) for _ in range(n)]

        for i in range(0, 2 * k, 2):
            dp[0][i] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])

            for j in range(1, 2 * k):
                if j % 2 != 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] - prices[i])
        
        return max(dp[-1])