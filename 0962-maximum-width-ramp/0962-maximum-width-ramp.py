class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        stack = [0]

        for i in range(1, n):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                res = max(res, j - i)

        return res