class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_counts = defaultdict(int)
        sum_counts[0] = 1
        curr_sum = 0
        count = 0

        for i in range(n):
            curr_sum += nums[i]
            target = curr_sum - k

            count += sum_counts[target]
            sum_counts[curr_sum] += 1
            
        return count
        

        