from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m, n = len(grid), len(grid[0])

        # dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

        # queue = deque()
        # fresh_count = 0
        # rotten_count = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             queue.append((i, j))
        #             rotten_count += 1
        #         elif grid[i][j] == 1:
        #             fresh_count += 1

        # if fresh_count == 0:
        #     return 0

        # if fresh_count > 0 and rotten_count == 0:
        #     return -1
        
        # time = -1
        # current_count = 0

        # while queue:
        #     size = len(queue)
        #     current_count += size
        #     time += 1

        #     for _ in range(size):
        #         i, j = queue.popleft()

        #         for k in range(4):
        #             next_i = i + dr[k]
        #             next_j = j + dc[k]

        #             if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
        #                 grid[next_i][next_j] = 2
        #                 queue.append((next_i, next_j))

        # if current_count < rotten_count + fresh_count:
        #     return -1

        # return time
        
        m, n = len(grid), len(grid[0])
        freshCount = 0
        rottenCount = 0

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    rottenCount += 1
                    queue.append((i, j))

        if freshCount == 0:
            return 0
        elif rottenCount == 0:
            return -1

        time = -1

        dr, dc = [1, -1, 0, 0], [0, 0, -1, 1] # down, up, left, right

        while queue:
            size = len(queue)
            time += 1

            for _ in range(size):
                row, col = queue.popleft()

                for k in range(4):
                    nextRow, nextCol = row + dr[k], col + dc[k]

                    if 0 <= nextRow < m and 0 <= nextCol < n and grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 2
                        freshCount -= 1
                        queue.append((nextRow, nextCol))

        if freshCount == 0:
            return time
        
        return -1


        
        

