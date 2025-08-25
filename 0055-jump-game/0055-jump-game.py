class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        currMax = 0

        for idx, step in enumerate(nums):
            if currMax < idx:
                return False

            currMax = max(currMax, idx + step) # max point we could reach after we reached index i

            if currMax >= len(nums) - 1:
                return True

        return False
