class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_counts = defaultdict(int)

        for num in nums:
            char_counts[num] += 1

        return heapq.nlargest(k, char_counts, key=char_counts.get)