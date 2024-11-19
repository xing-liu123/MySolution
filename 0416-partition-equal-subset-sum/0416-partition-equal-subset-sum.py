class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        target = totalSum // 2

        dp = [0] * (target + 1)

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = max(dp[i], num + dp[i - num])
            
            if dp[target] == target:
                return True

        return False

        