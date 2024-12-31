class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1] # right, left, up, down
        count = 0

        def dfs(row, col):
            grid[row][col] = "0"

            for k in range(4):
                next_row = row + dr[k]
                next_col = col + dc[k]

                if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == "1":
                    dfs(next_row, next_col)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


        # count = 0

        # def bfs(x, y):
        #     queue = deque([(x, y)])
        #     grid[x][y] = "0"

        #     while queue:
        #         size = len(queue)

        #         for _ in range(size):
        #             x, y = queue.pop()
        #             for k in range(4):
        #                 nx, ny = x + dr[k], y + dc[k]

        #                 if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
        #                     queue.appendleft((nx, ny))
        #                     grid[nx][ny] = "0"

        
















        # m, n = len(grid), len(grid[0])
        # dr = [0, 0, 1, -1]
        # dc = [1, -1, 0, 0]
        # visited = [[False] * n for _ in range(m)]

        # count = 0

        # # def dfs(row, col) :
        # #     if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or grid[row][col] == "0":
        # #         return
        # #     else:
        # #         visited[row][col] = True
        # #         for k in range(4):
        # #             dfs(row + dr[k], col + dc[k])

        # def bfs(row, col):
        #     queue = deque()
        #     queue.append([row, col])
        #     visited[row][col] = True
        #     while queue:
        #         size = len(queue)

        #         for _ in range(size):
        #             curr = queue.popleft()

        #             for i in range(4):
        #                 x = curr[0] + dr[i]
        #                 y = curr[1] + dc[i]

        #                 if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == "1" and not visited[x][y]:
        #                     queue.append([x, y])
        #                     visited[x][y] = True


        # for i in range(m):
        #     for j in range(n):
        #         if not visited[i][j] and grid[i][j] == "1":
                   
        #             count += 1
        #             # dfs(i, j)
        #             bfs(i, j)
        
        # return count
            