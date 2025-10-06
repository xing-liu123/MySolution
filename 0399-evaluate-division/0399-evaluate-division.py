from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = defaultdict(float)

        for (u, v), value in zip(equations, values):
            graph[u].append(v)
            graph[v].append(u)
            res[(u, v)] = value
            res[(v, u)] = 1.0 / value

        def dfs(curr, start, end, currVal, visited):
            if curr == end:
                return
            
            visited.add(curr)

            for nextNode in graph[curr]:
                if nextNode not in visited:
                    res[(start, nextNode)] = currVal * res[(curr, nextNode)]
                    dfs(nextNode, start, end, res[(start, nextNode)], visited)

        results = []
        for u, v in queries:
            if u not in graph or v not in graph:
                results.append(-1.0)
                continue

            if u == v:
                results.append(1.0)
                continue

            if (u, v) in res:
                results.append(res[(u, v)])
            else:
                dfs(u, u, v, 1, set())

                if (u, v) in res:
                    results.append(res[(u, v)])
                else:
                    results.append(-1)

        return results


        
            


            
