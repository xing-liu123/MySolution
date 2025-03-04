class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)

        maxLen = 0

        for i in range(len(nums) - 1, -1, -1):
            left = len(nums)
            while stack and nums[i] >= nums[stack[-1]]:
                left = stack.pop()
            
            maxLen = max(maxLen, i - left)

            if not stack:
                break

        return maxLen