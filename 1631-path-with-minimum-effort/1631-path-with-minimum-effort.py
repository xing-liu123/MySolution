from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m, n = len(heights), len(heights[0])

        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        dist_map = dict()
        dist_map[(0, 0)] = 0

        queue = deque([(0, 0)])

        while queue:
            x, y = queue.popleft()

            for k in range(4):
                next_x, next_y = dr[k] + x, dc[k] + y

                if 0 <= next_x < m and 0 <= next_y < n:
                    dist = max(dist_map[(x, y)], abs(heights[x][y] - heights[next_x][next_y]))
                    if not (next_x, next_y) in dist_map or dist < dist_map[(next_x, next_y)]:
                        queue.append((next_x, next_y))
                        dist_map[(next_x, next_y)] = dist

        return dist_map[(m - 1, n - 1)]
            
            
                