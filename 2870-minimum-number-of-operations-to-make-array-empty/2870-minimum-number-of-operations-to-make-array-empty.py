class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numCounts = defaultdict(int)

        for num in nums:
            numCounts[num] += 1

        res = 0

        for c in numCounts.values():
            if c == 1:
                return -1
            elif c % 3 == 0:
                res += c // 3
            else:
                res += (c // 3 + 1)
        
        return res
