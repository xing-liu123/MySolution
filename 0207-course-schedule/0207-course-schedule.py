from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u, v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        visited = 0

        while queue:
            course = queue.popleft()
            visited += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return visited == numCourses

        
