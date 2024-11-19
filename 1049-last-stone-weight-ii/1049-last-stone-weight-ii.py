class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        totalSum = sum(stones)
        target = totalSum // 2

        dp = [0] * (target + 1)

        for stone in stones:
            for i in range(target, stone - 1, -1):
                dp[i] = max(dp[i], stone + dp[i - stone])

            if dp[target] == target:
                return totalSum - 2 * target

        return totalSum - 2 * dp[target]
