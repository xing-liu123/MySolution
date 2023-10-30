class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        dp = [1] * n
        counts = [1] * n

        maxLen = 0

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                         dp[i] = dp[j] + 1
                         counts[i] = counts[j]
                    elif dp[j] + 1 == dp[i]:
                        counts[i] += counts[j]
                
                maxLen = max(maxLen, dp[i])
        
        
        res = 0

        for i in range(n):
            if dp[i] == maxLen:
                res += counts[i]
        
        return res