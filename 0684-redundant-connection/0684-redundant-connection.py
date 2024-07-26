from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(1001)]
        rank = [0] * 1001

        def find(u) -> int:
            if parents[u] != u:
                parents[u] = find(parents[u])
            
            return parents[u]

        def join(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if rank[u] > rank[v]:
                    parents[root_v] = root_u
                elif rank[u] < rank[v]:
                    parents[root_u] = root_v
                else:
                    parents[root_v] = root_u
                    rank[root_u] += 1
        
        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                join(u, v)
        
        return None
            


        
        
        


        