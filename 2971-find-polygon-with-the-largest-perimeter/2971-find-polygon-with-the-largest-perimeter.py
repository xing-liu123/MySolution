class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        preSum = [0] * n
        preSum[0] = nums[0]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i]

        res = preSum[2] if nums[0] < preSum[2] - nums[0] else -1
        left = 0

        for right in range(3, len(nums)):
            
            while left + 1 < right - 1 and preSum[right] - preSum[left] <= nums[left]:
                left += 1

            if preSum[right] - preSum[left] > nums[left]:
                res = max(res, preSum[right] - preSum[left] + nums[left])
            
        return res



            