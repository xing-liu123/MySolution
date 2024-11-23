class Solution:
    class Union:
        def __init__(self):
            self.parents = list(range(1005))
            
        def find(self, u):
            if self.parents[u] != u:
                self.parents[u] = self.find(self.parents[u])

            return self.parents[u]

        def join(self, u, v):
            parent_u = self.find(u)
            parent_v = self.find(v)

            if parent_u != parent_v:
                self.parents[parent_v] = parent_u

        def isSame(self, u, v):
            return self.find(u) == self.find(v)


    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(1005))
        candidate1 = candidate2 = None

        for u, v in edges:
            if parents[v] != v:
                candidate1 = [parents[v], v]
                candidate2 = [u, v]
                break
            
            parents[v] = u
            

        union = self.Union()

        for u, v in edges:
            if [u, v] == candidate2:
                continue

            if union.isSame(u, v):
                if candidate1:
                    return candidate1
                else:
                    return [u, v]
            else:
                union.join(u, v)

        return candidate2
            