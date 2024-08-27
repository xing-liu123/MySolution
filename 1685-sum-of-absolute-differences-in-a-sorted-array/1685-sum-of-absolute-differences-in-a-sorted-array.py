class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(1, n):
            res[0] += (nums[i] - nums[0])

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            res[i] = res[i - 1] - (n - 2 * i) * diff

        return res