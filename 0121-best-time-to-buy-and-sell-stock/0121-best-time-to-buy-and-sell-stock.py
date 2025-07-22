class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMinPrice = prices[0]
        currMaxProfit = 0

        for price in prices[1:]:
            if price < currMinPrice:
                currMinPrice = price

            currMaxProfit = max(currMaxProfit, price - currMinPrice)

        return currMaxProfit