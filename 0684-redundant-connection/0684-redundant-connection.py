class Union:
        def __init__(self):
            self.parents = list(range(1005))
            self.ranks = [1] * 1005
        
        def find(self, u):
            if self.parents[u] != u:
                self.parents[u] = self.find(self.parents[u])

            return self.parents[u]

        def join(self, u, v):
            parent_u = self.find(u)
            parent_v = self.find(v)

            if parent_u != parent_v:
                if self.ranks[parent_u] > self.ranks[parent_v]:
                    self.parents[parent_v] = parent_u
                elif self.ranks[parent_u] < self.ranks[parent_v]:
                    self.parents[parent_u] = parent_v
                else:
                    self.parents[parent_v] = parent_u
                    self.ranks[parent_u] += 1

        def isSame(self, u, v):
            return self.find(u) == self.find(v)

class Solution:
    

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = Union()

        for edge in edges:
            u, v = edge

            if union.isSame(u, v):
                return edge
            else:
                union.join(u, v)

            