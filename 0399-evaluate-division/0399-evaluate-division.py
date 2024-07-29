class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            u, v = equations[i]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))

        visited = dict()

        def dfs(curr):
            visited[curr] = dict()
            visited[curr][curr] = 1

            for next_node, dist in graph[curr]:
                if not next_node in visited:
                    dfs(next_node)
                for next_next, next_dist in visited[next_node].items():
                    visited[curr][next_next] = dist * next_dist

        res = []

        for u, v in queries:
            if not u in graph or not v in graph:
                res.append(-1)
            else:
                if not u in visited or not v in visited[u]:
                    dfs(u)

                if v in visited[u]:
                    res.append(visited[u][v])
                else:
                    res.append(-1)
        
        return res




