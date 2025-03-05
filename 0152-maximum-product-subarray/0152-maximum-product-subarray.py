class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_dp = nums[0]
        min_dp = nums[0]
        res = nums[0]
        for i in range(1, n):
            num = nums[i]

            if num < 0:
                max_dp, min_dp = min_dp, max_dp

            max_dp = max(num, num*max_dp)
            min_dp = min(num, num*min_dp)

            res = max(res, max_dp)

        return res