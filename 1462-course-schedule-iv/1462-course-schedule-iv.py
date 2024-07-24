class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)

        for u, v in prerequisites:
            graph[u].add(v)

        visited = set()

        def dfs(curr):
            visited.add(curr)

            if not graph[curr]:
                return

            new_set = set()
            for next_node in graph[curr]:
                if not next_node in visited:
                    dfs(next_node)
                
                for next_next in graph[next_node]:
                    new_set.add(next_next)
            
            for next_next in new_set:
                graph[curr].add(next_next)

        res = []

        for u, v in queries:
            if not u in visited:
                dfs(u)
                
            if v in graph[u]:
                res.append(True)
            else:
                res.append(False)

        return res