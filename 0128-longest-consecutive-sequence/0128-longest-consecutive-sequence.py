class UnionFind:
    def __init__(self):
        self.parents = {}
        self.counts = {}
        self.max = 1

    def find(self, u):
        if not u in self.parents:
            self.parents[u] = u
            self.counts[u] = 1
            return u
        
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])

        return self.parents[u]

    def join(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            self.counts[rootV] += self.counts[rootU]
            self.parents[rootU] = rootV
            self.max = max(self.max, self.counts[rootV])
            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)

        union = UnionFind()

        for num in numSet:
            if num - 1 in numSet:
                union.join(num, num - 1)
            
            if num + 1 in numSet:
                union.join(num, num + 1)

        return union.max
