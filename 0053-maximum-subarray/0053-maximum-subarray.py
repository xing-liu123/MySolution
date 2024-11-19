class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        res = curr

        for num in nums[1:]:
            curr = max(curr + num, num)
            res = max(curr, res)

        return res