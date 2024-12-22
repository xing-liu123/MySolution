class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u, v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)
        
        def dfs(curr):
            indegree[curr] -= 1

            for next_course in graph[curr]:
                indegree[next_course] -= 1
                
                if indegree[next_course] == 0:
                    dfs(next_course)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i) 

        return sum(indegree) == -numCourses

