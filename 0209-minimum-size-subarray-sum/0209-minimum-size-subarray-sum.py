class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLength = sys.maxsize

        for right in range(len(nums)):
            currSum += nums[right]

            if currSum >= target:
                while currSum - nums[left] >= target:
                    currSum -= nums[left]
                    left += 1
                minLength = min(minLength, right - left + 1)

        return 0 if minLength == sys.maxsize else minLength


