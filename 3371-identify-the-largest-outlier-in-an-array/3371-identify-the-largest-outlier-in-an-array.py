class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        largest_outlier = float("-inf")
        num_counts = Counter(nums)

        for num in nums:
            candidate = total_sum - 2 * num

            if candidate in num_counts:
                if candidate != num or num_counts[num] > 1:
                    largest_outlier = max(largest_outlier, candidate)

        return largest_outlier

