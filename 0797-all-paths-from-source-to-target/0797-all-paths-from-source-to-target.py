class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]
        target = len(graph) - 1

        def backtracking(curr):
            if curr == target:
                res.append(path.copy())
                return
            
            for node in graph[curr]:
                path.append(node)
                backtracking(node)
                path.pop()

        backtracking(0)

        return res
