class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, u) -> int:
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]

    def union(self, u, v) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.root[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.root[root_u] = root_v
            else:
                self.root[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def findMST(self, n, edges, include=None, exclude=None):
        uf = UnionFind(n)   
        cost = 0
        edge_count = 0

        if include is not None:
            uf.union(edges[include][0], edges[include][1])
            cost += edges[include][2]
            edge_count += 1

        for i, (u, v, w, _) in enumerate(edges):
            if i == exclude:
                continue
            
            if uf.union(u, v):
                cost += w
                edge_count += 1
            
            if edge_count == n - 1:
                break

        return cost if edge_count == n - 1 else float('inf')

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        sorted_edges = sorted([[u, v, w, i] for i, [u, v, w] in enumerate(edges)], key=lambda x: x[2])
        
        min_weights = self.findMST(n, sorted_edges)

        critical = []
        non_critical = []

        for i in range(len(sorted_edges)):
            if self.findMST(n, sorted_edges, exclude=i) > min_weights:
                critical.append(sorted_edges[i][3])
            elif self.findMST(n, sorted_edges, include=i) == min_weights:
                non_critical.append(sorted_edges[i][3])
        
        return [critical, non_critical]