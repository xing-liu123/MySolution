class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        num_counts = Counter(nums)
        max_outlier = min(nums)

        for num in num_counts.keys():
            potential_outlier = total_sum - 2 * num

            if potential_outlier in num_counts:
                if potential_outlier != num or num_counts[num] > 1:
                    max_outlier = max(potential_outlier, max_outlier)

        return max_outlier

