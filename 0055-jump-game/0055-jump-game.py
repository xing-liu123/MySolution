class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        curr_idx = 0

        while curr_idx < len(nums) - 1 and curr_idx <= curr_max:
            curr_max = max(curr_max, curr_idx + nums[curr_idx])

            if curr_max <= curr_idx:
                return False

            curr_idx += 1

        return curr_idx == len(nums) - 1
