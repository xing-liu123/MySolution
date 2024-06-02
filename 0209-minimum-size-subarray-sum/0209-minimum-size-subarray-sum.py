class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = sys.maxsize
        
        left = 0
        currSum = 0
        
        for right in range(len(nums)):
            if nums[right] >= target:
                return 1
            
            currSum += nums[right]
            
            while currSum >= target:
                minLen = min(minLen, right - left + 1)
                currSum -= nums[left]
                left += 1
        
        return minLen if minLen != sys.maxsize else 0
        
