class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        sum_map = defaultdict(lambda: 0)
        sum_map[0] = 1

        count = 0

        for s in nums:
            count += sum_map[s - k]
            sum_map[s] += 1            

        return count
