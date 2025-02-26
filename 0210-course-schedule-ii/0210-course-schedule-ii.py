from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph = defaultdict(list)
        # indegree = [0] * numCourses

        # for u, v in prerequisites:
        #     graph[v].append(u)
        #     indegree[u] += 1

        # queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # order = []

        # while queue:
        #     course = queue.popleft()
        #     order.append(course)

        #     for next_course in graph[course]:
        #         indegree[next_course] -= 1

        #         if indegree[next_course] == 0:
        #             queue.append(next_course)

        # return order if len(order) == numCourses else []

        # graph = defaultdict(list)

        # for course, preq in prerequisites:
        #     graph[preq].append(course)


        # order = []
        # has_cycle = False

        # visited = [0] * numCourses # 0: unvisited, 1: visiting, 2: visited

        # def dfs(course):
        #     nonlocal has_cycle

        #     if visited[course] == 1:
        #         has_cycle = True
        #         return
            
        #     if visited[course] == 2:
        #         return

        #     visited[course] = 1

        #     for neighbor in graph[course]:
        #         dfs(neighbor)

        #     order.append(course)
        #     visited[course] = 2

        
        # for i in range(numCourses):
        #     if visited[i] == 0:
        #         dfs(i)
        #         if has_cycle:
        #             return []

        # return order[::-1]

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []

        while queue:
            course = queue.popleft()
            res.append(course)

            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1

                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return res if len(res) == numCourses else []






        