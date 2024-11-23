class Union:
        def __init__(self):
            self.parents = list(range(1005))
        
        def find(self, u):
            parent_u = self.parents[u]
            if parent_u == u:
                return u
            else:
                return self.find(parent_u)

        def join(self, u, v):
            parent_u = self.find(u)
            parent_v = self.find(v)

            self.parents[parent_v] = parent_u

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

            