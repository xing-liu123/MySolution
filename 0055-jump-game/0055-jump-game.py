class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        currMax = 0

        for i in range(n):
            if i > currMax:
                return False
            currMax = max(currMax, i + nums[i])
            
            if currMax >= n - 1:
                return True

        return currMax >= n - 1