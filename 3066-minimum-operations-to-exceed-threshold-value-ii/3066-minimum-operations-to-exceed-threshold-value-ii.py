class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        while nums[0] < k:
            count += 1
            val1 = heapq.heappop(nums)
            val2 = heapq.heappop(nums)

            val3 = min(val1, val2) * 2 + max(val1, val2)
            heapq.heappush(nums, val3)

        return count