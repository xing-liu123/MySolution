class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        curr_min = prices[0]

        for i in range(1, n):
            if prices[i] >= curr_min:
                max_profit = max(max_profit, prices[i] - curr_min)
            else:
                curr_min = prices[i]

        return max_profit