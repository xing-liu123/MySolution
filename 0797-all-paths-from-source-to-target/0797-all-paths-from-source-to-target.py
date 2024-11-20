class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]
        res = []

        def dfs(curr):
            if curr == len(graph) - 1:
                res.append(copy.copy(path))
                return
            
            for edge in graph[curr]:
                path.append(edge)
                dfs(edge)
                path.pop()

        dfs(0)
        return res