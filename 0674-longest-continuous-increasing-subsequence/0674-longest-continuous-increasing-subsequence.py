class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        left = 0
        res = 1


        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                left = i
            else:
                res = max(res, i - left + 1)
        
        return res