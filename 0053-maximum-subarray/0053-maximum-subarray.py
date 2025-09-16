class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = float('-inf')
        res = float('-inf')

        for num in nums:
            currMax = max(currMax + num, num)
            res = max(res, currMax)

        return res