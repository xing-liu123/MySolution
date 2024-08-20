class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        sum_map = {}
        sum_map[0] = 1

        count = 0

        for s in nums:
            if s - k in sum_map:
                count += sum_map[s - k]
            
            if s in sum_map:
                sum_map[s] += 1
            else:
                sum_map[s] = 1

        return count
