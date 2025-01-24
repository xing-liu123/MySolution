from collections import deque

class Trie:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def join(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            self.parent[root_u] = root_v

    def add(self, u):
        if u not in self.parent:
            self.parent[u] = u


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        trie = Trie()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    trie.add((i, j))
                    if i > 0 and grid[i - 1][j] == "1":
                        trie.join((i, j), (i - 1, j))

                    if j > 0 and grid[i][j - 1] == "1":
                        trie.join((i, j), (i, j - 1))

        unique_roots = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    unique_roots.add(trie.find((i, j)))

        return len(unique_roots)

        # def dfs(row, col):
        #     grid[row][col] = "0"

        #     for k in range(4):
        #         next_row = row + dr[k]
        #         next_col = col + dc[k]

        #         if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == "1":
        #             dfs(next_row, next_col)

        # def bfs(row, col):
        #     queue = deque([(row,col)])
        #     grid[row][col] = "0"

        #     while queue:
        #         node = queue.popleft()

        #         for k in range(4):
        #             next_row = node[0] + dr[k]
        #             next_col = node[1] + dc[k]

        #             if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == "1":
        #                 grid[next_row][next_col] = "0"
        #                 queue.append((next_row, next_col))
        
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1":
        #             count += 1
        #             # dfs(i, j)
        #             bfs(i, j)

        # return count


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
            