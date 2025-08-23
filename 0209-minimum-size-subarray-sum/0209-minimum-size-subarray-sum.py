class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0

        length = float("inf")
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum - nums[left] >= target:
                currSum -= nums[left]
                left += 1
            
            if currSum >= target:
                length = min(length, right - left + 1)
        
        return length if length != float("inf") else 0
