class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # x = nums[0]
        # y = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     z = y
        #     y = max(x + nums[i], y)
        #     x = z

        # return max(x, y) 
        
        if len(nums) == 1:
            return nums[0]

        x = nums[0]
        y = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            z = y
            y = max(y, x + nums[i])
            x = z
        
        return y