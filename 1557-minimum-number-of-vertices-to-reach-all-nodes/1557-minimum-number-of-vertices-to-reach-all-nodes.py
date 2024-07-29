class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        

        min_set = sys.maxsize

        for _, v in edges:
            graph[v] += 1
            min_set = min(min_set, graph[v])

        if len(graph) != n:
            return [i for i in range(n) if i not in graph]
        else:
            return [i for i in range(n) if graph[i] == min_set]

        
