class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        max_sum = float("-inf")

        for i, num in enumerate(nums):
            curr_sum += num

            if i >= k:
                curr_sum -= nums[i - k]

            if i >= k - 1:
                max_sum = max(max_sum, curr_sum)

        return max_sum / k
            