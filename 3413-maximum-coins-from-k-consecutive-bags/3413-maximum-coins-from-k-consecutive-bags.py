class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def getMaximumCoins(coins):
            coins.sort()

            n = len(coins)
            res = curr = j = 0

            for i in range(n):
                curr += (coins[i][1] - coins[i][0] + 1) * coins[i][2]

                while coins[j][1] < coins[i][1] - k + 1:
                    curr -= (coins[j][1] - coins[j][0] + 1) * coins[j][2]
                    j += 1
                
                part = max(0, coins[i][1] - k - coins[j][0] + 1) * coins[j][2]
                res = max(res, curr - part)
            
            return res

        return max(getMaximumCoins(coins), getMaximumCoins([[-r, -l, w] for l, r, w in coins]))
            

            
