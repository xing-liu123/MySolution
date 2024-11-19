class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mins = [0] * n

        currMin = sys.maxsize

        for i in range(n):
            mins[i] = currMin
            currMin = min(currMin, prices[i])
        currMax = prices[-1]
        maxProfit = 0

        for i in range(n - 1, -1, -1):
            currMax = max(prices[i], currMax)
            maxProfit = max(maxProfit, currMax - mins[i])

        return maxProfit


        