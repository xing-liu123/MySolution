class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        reachable = [[False] * numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            reachable[i][i] = True

        def dfs(curr):
            for next_node in graph[curr]:
                if not reachable[curr][next_node]:
                    reachable[curr][next_node]
                    dfs(next_node)
                
                for k in range(numCourses):
                    if reachable[next_node][k]:
                        reachable[curr][k] = True

        for i in range(numCourses):
            dfs(i)

        res = [reachable[u][v] for u, v in queries]

        return res