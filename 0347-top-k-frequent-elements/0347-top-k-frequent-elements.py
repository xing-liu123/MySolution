class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        if len(counts) <= k:
            return [val for val in counts.keys()]

        return heapq.nlargest(k, counts, key=counts.get)