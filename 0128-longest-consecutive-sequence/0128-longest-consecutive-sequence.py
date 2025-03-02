# class UnionFind:
#     def __init__(self):
#         self.parents = {}
#         self.counts = {}
#         self.max = 1

#     def find(self, u):
#         if not u in self.parents:
#             self.parents[u] = u
#             self.counts[u] = 1
#             return u
        
#         if self.parents[u] != u:
#             self.parents[u] = self.find(self.parents[u])

#         return self.parents[u]

#     def join(self, u, v):
#         rootU = self.find(u)
#         rootV = self.find(v)

#         if rootU != rootV:
#             if self.counts[rootU] > self.counts[rootV]:  # Merge smaller into larger
#                 rootU, rootV = rootV, rootU

#             self.parents[rootU] = rootV
#             self.counts[rootV] += self.counts[rootU]
#             self.max = max(self.max, self.counts[rootV])
            


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0

        # numSet = set(nums)

        # union = UnionFind()

        # for num in numSet:
        #     if num - 1 in numSet:
                
        #         union.join(num, num - 1)
            

        # return union.max

        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            if not num - 1 in numSet:
                currNum = num
                currLen = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currLen += 1

                maxLen = max(currLen, maxLen)

        return maxLen
