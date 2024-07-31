from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        
        visited = set()
        queue = deque([(n, 0)])

        while queue:
            curr, days = queue.popleft()

            if curr in visited:
                continue

            if curr == 0:
                return days

            visited.add(curr)

            if curr % 3 == 0 and curr // 3 not in visited:
                queue.append((curr // 3, days + 1))

            if curr % 2 == 0 and curr // 2 not in visited:
                queue.append((curr // 2, days + 1))
            
            if curr - 1 not in visited:
                queue.append((curr - 1, days + 1))

        return -1
        