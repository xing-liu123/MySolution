class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u, v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)

        visited = set()
        
        def dfs(curr):
            visited.add(curr)

            for next_course in graph[curr]:
                indegree[next_course] -= 1
                
                if not next_course in visited and indegree[next_course] == 0:
                    dfs(next_course)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i) 

        return len(visited) == numCourses

