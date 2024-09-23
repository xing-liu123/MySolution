class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [1] * len(nums)
        prev = [-1] * len(nums)

        max_len = 1
        max_idx = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 >  dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_idx = i

        res = []
        idx = max_idx

        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]

        return res

        

            
            