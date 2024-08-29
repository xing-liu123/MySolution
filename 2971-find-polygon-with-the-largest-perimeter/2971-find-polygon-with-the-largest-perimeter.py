class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        preSum = [0] * n
        preSum[0] = nums[0]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i]

        for i in range(n - 2):
            if preSum[n - 1] - preSum[i] > nums[i]:
                return preSum[n - 1] - preSum[i] + nums[i]
            
        return -1



            