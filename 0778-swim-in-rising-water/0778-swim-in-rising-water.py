class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        min_heap = [(grid[0][0], 0, 0)]
        time_map = defaultdict(lambda: sys.maxsize)
        time_map[(0, 0)] = grid[0][0]

        while min_heap:
            t, x, y = heapq.heappop(min_heap)

            if x == n - 1 and y == n - 1:
                return t


            for k in range(4):
                nx, ny = x + dr[k], y + dc[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if not (nx, ny) in time_map:
                        
                        if t >= grid[nx][ny]:
                            heapq.heappush(min_heap, (t, nx, ny))
                            time_map[(nx, ny)] = t
                        else:
                            heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
                            time_map[(nx, ny)] = grid[nx][ny]
                    elif grid[nx][ny] <= t < time_map[(nx, ny)]:
                        heapq.heappush(min_heap, (t, nx, ny))
                        time_map[(nx, ny)] = t
        return -1
        