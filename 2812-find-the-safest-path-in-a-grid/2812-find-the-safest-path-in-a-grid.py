from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        distances = [[0] * n for _ in range(n)]

        queue = deque()
        visited = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                for k in range(4):
                    next_x, next_y = x + dr[k], y + dc[k]
                    
                    if 0 <= next_x < n and 0 <= next_y < n and not (next_x, next_y) in visited:
                        queue.append((next_x, next_y))
                        distances[next_x][next_y] = distances[x][y] + 1
                        visited.add((next_x, next_y))
        
        

        # max_heap = [(-distances[0][0], 0, 0)]

        # dist_map = defaultdict(lambda: 0)
        # dist_map[(0, 0)] = distances[0][0]


        # while max_heap:
        #     dist, x, y = heapq.heappop(max_heap)
        #     dist = - dist

        #     for k in range(4):
        #         next_x, next_y = x + dr[k], y + dc[k]
        #         if 0 <= next_x < n and 0 <= next_y < n:
        #             next_dist = min(dist, distances[next_x][next_y])

        #             if next_dist > dist_map[(next_x, next_y)]:
        #                 heapq.heappush(max_heap, (-next_dist, next_x, next_y))
        #                 dist_map[(next_x, next_y)] = next_dist

        # return dist_map[(n - 1, n - 1)]
        

        def canReach(safeness) -> bool:
            if safeness == 0:
                return True

            
            new_distances = [[distances[i][j] if distances[i][j] >= safeness else 0 for j in range(n)] for i in range(n)]
            
            if new_distances[0][0] == 0:
                return False

            queue = deque([(0, 0)])

            new_distances[0][0] = 0

            while queue:
                x, y = queue.popleft()

                if x == n - 1 and y == n - 1:
                    return True

                for k in range(4):
                    next_x, next_y = x + dr[k], y + dc[k]
                    if 0 <= next_x < n and 0 <= next_y < n and new_distances[next_x][next_y] != 0:
                        queue.append((next_x, next_y))
                        new_distances[next_x][next_y] = 0

            return False

        left = 0
        right = max(max(row) for row in distances)

        while left <= right:
            mid = left + (right - left) // 2
            if canReach(mid):
                left = mid + 1
            else:
                right = mid - 1
            

        return right