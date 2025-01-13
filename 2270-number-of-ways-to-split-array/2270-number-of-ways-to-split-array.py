class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        count = 0
        curr_sum = 0

        for i in range(len(nums) - 1):
            curr_sum += nums[i]
            remaining = total_sum - curr_sum

            if curr_sum >= remaining:
                count += 1

        return count