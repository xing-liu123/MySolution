class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return False
        
        if n == 2:
            return nums[0] == nums[1]
        
        if sum(nums) % 2 != 0:
            return False

        target = int(sum(nums) / 2)

        dp = [0] * (target + 1)

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + num)
        
        return dp[target] == target
