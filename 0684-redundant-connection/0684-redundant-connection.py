from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(1001)]

        def find(u) -> int:
            if parents[u] == u:
                return u
            
            parents[u] = find(parents[u])

            return parents[u]

        def join(u, v):
            u = find(u)
            v = find(v)

            if u == v:
                return

            parents[v] = u

        def isSame(u, v) -> bool:
            return find(u) == find(v)
        
        for u, v in edges:
            if isSame(u, v):
                return [u, v]
            else:
                join(u, v)
        
        return None
            


        
        
        


        