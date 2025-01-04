class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0

        for i in range(len(nums)):
            if i > curr_max:
                return False

            curr_max = max(curr_max, i + nums[i])

            if curr_max >= len(nums) - 1:
                return True

        return False