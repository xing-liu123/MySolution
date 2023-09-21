class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if (total_sum + target) % 2 != 0:
            return 0
        
        if target < 0 and total_sum < -target:
            return 0
        
        myTarget = (total_sum + target) // 2

        dp = [0] * (myTarget + 1)
        dp[0] = 1

        for num in nums:
            for i in range(myTarget, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[myTarget]