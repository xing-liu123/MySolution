from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        
        visited = dict()
        queue = deque([(n, 0)])

        while queue:
            curr, days = queue.popleft()

            if curr == 0:
                return days

            visited[curr] = days

            if curr % 3 == 0 and (curr // 3 not in visited or days + 1 < visited[curr // 3]):
                queue.append((curr // 3, days + 1))

            if curr % 2 == 0 and (curr // 2 not in visited or days + 1 < visited[curr // 2]):
                queue.append((curr // 2, days + 1))
            
            if curr - 1 not in visited or days + 1 < visited[curr - 1]:
                queue.append((curr - 1, days + 1))

        return -1
        