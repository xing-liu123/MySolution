class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - currMin)

        return maxProfit
            