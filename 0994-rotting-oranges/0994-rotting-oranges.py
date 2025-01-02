from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        queue = deque()
        orange_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

                if grid[i][j] != 0:
                    orange_count += 1

        time = -1
        current_count = 0

        while queue:
            size = len(queue)
            current_count += size
            time += 1

            for _ in range(size):
                i, j = queue.popleft()

                for k in range(4):
                    next_i = i + dr[k]
                    next_j = j + dc[k]

                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                        grid[next_i][next_j] = 2
                        queue.append((next_i, next_j))

        if current_count < orange_count:
            return -1

        return time