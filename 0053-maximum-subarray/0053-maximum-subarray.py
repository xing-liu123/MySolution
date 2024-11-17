class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = -sys.maxsize - 1


        for i in range(n):
            count += nums[i]
            res = max(res, count)
        

            if count <= 0:
                count = 0

        return res