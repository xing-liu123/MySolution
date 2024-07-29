class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)

        for _, v in edges:
            graph[v] += 1

        if len(graph) != n:
            return [i for i in range(n) if i not in graph]
        else:
            min_set = min(graph)
            return [i for i in range(n) if graph[i] == min_set]

        
