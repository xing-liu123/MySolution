class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        x = 0
        y = -prices[0] # hold stock

        for i in range(1, n):
            x = max(y + prices[i], x)
            y = max(-prices[i], y) 

        return max(x, y)