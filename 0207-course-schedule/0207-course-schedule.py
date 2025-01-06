from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            course_map[preq].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        visited = 0

        while queue:
            course = queue.popleft()
            visited += 1

            for next_course in course_map[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return visited == numCourses
            



        
