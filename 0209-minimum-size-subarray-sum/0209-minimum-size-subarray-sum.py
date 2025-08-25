class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minLen = float("inf")
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum - nums[left] >= target:
                currSum -= nums[left]
                left += 1

            if currSum >= target:
                minLen = min(minLen, right - left + 1)

        return minLen if minLen != float('inf') else 0