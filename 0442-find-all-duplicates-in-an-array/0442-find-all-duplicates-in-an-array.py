class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        return [k for k, v in counts.items() if v > 1]