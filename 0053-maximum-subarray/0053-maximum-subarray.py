class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        lastMax = nums[0]
        res = nums[0]


        for i in range(1, n):
            lastMax = max(lastMax + nums[i], nums[i])
            res = max(res, lastMax)

        return res