class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = dict()

        def dfs(curr):
            if not graph[curr]:
                visited[curr] = True
                return
            visited[curr] = False
            count = 0

            for neighbor in graph[curr]:
                if not neighbor in visited:
                    dfs(neighbor)
                
                if visited[neighbor]:
                    count += 1
            
            visited[curr] = count == len(graph[curr])

        for i in range(len(graph)):
            if not i in visited:
                dfs(i)
            
            if visited[i]:
                res.append(i)

        return res