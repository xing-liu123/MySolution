class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = 0
        res = float("-inf")

        for num in nums:
            curr = max(curr + num, num)
            res = max(curr, res)

        return res