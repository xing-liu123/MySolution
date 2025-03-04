class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        totalPairs = n * (n - 1) // 2
        goodPairs = 0
        numFreq = defaultdict(int)

        for i in range(n):
            key = nums[i] - i
            goodPairs += numFreq[key]

            numFreq[key] += 1

        return totalPairs - goodPairs