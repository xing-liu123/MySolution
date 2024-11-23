class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(curr):
            visited.add(curr)
            if curr == destination:
                return True

            for next_node in graph[curr]:
                if not next_node in visited:
                    if dfs(next_node):
                        return True

            return False 

        return dfs(source)

