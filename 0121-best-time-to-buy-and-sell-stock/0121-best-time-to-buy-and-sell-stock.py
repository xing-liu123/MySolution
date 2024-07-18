class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_price)
            min_price = min(prices[i], min_price)
        
        return profit