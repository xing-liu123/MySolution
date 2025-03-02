class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize] * n
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]