class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        x = nums[0]
        y = max(nums[0], nums[1])
        z = 0

        for i in range(2, len(nums)):
            z = max(y, x + nums[i])
            x = y
            y = z
        
        return y