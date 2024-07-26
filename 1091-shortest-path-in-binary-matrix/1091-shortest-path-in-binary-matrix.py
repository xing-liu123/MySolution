from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1:
            return -1

        dr, dc = [1, 1, 1, -1, -1, -1, 0, 0], [0, 1, -1, 0, 1, -1, 1, -1]
        queue = deque([(0, 0)])
        grid[0][0] = 1
        length = 1

        while queue:
            size = len(queue)

            for _ in range(size):
                cell = queue.popleft()

                if cell == (n - 1, n - 1):
                    return length

                for k in range(8):
                    x = cell[0] + dr[k]
                    y = cell[1] + dc[k]

                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        queue.append((x, y))
                        grid[x][y] = 1

            length += 1

        return -1

