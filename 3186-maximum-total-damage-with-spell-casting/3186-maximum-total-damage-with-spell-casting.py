from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        sortedPower = sorted(count)

        n = len(sortedPower)

        if n == 1:
            return sortedPower[0] * count[sortedPower[0]]

        dp = [0] * len(sortedPower)
        
        dp[0] = sortedPower[0] * count[sortedPower[0]]
        dp[1] = dp[0]

        if sortedPower[1] > sortedPower[0] + 2:
            dp[1] += sortedPower[1] * count[sortedPower[1]]
        else:
            dp[1] = max(dp[0], sortedPower[1] * count[sortedPower[1]])

        for i in range(2, len(sortedPower)):
            if sortedPower[i - 2] + 2 >= sortedPower[i]:
                if i > 2:
                    dp[i] = max(dp[i - 1], dp[i - 3] + sortedPower[i] * count[sortedPower[i]])
                else:
                    dp[i] = max(dp[i - 1], sortedPower[i] * count[sortedPower[i]])
            elif sortedPower[i - 1] + 2 >= sortedPower[i]:
                dp[i] = max(dp[i - 1], dp[i - 2] + sortedPower[i] * count[sortedPower[i]])
            else:
                dp[i] = dp[i - 1] + sortedPower[i] * count[sortedPower[i]]

        return dp[-1]