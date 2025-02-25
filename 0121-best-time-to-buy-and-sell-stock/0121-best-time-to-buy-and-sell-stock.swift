class Solution {
    func maxProfit(_ prices: [Int]) -> Int {
        if prices.count == 1 {
            return 0
        }

        var currMin = prices[0]
        var maxProfit = 0

        for i in 1..<prices.count {
            if prices[i] < currMin {
                currMin = prices[i]
            } else if prices[i] - currMin > maxProfit {
                maxProfit = prices[i] - currMin
            }
        }

        return maxProfit
    }
}