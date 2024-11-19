class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        

        res = curr

        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            res = max(res, curr)

        return res