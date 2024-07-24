class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        reachable = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            reachable[u][v] = True

        

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
            

        res = [reachable[u][v] for u, v in queries]

        return res