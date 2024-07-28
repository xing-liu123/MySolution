class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parents = [i for i in range(n + 1)]

        def find(u) -> int:
            if parents[u] != u:
                parents[u] = find(parents[u])
            
            return parents[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parents[root_u] = parents[root_v]

        for u, v, _ in roads:
            if find(u) != find(v):
                union(u, v)
        
        res = sys.maxsize

        for u, v, z in roads:
            if find(u) == find(1):
                res = min(res, z)

        return res

 
