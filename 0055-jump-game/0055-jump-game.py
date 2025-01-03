class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_idx = 0
        curr_max = 0

        while curr_idx <= curr_max:
            curr_max = max(curr_max, curr_idx + nums[curr_idx])
            curr_idx += 1
            if curr_max >= n - 1:
                return True

        return curr_max >= n - 1
