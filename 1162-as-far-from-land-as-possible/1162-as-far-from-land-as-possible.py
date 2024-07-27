from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i ,j))
        
        if len(queue) == n * n or len(queue) == 0:
            return -1
 
        length = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                cell = queue.popleft()

                for k in range(4):
                    x = cell[0] + dr[k]
                    y = cell[1] + dc[k]

                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        queue.append((x, y))
                        grid[x][y] = 1
                
            length += 1
        
        return length - 1