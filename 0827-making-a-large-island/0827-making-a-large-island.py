class Solution:
    def __init__(self):
        self.areas = defaultdict(int)
        self.grid = []
        self.dr = [1, -1, 0, 0]
        self.dc = [0, 0, 1, -1]
        self.m = 0
        self.n = 0
        self.visited = []

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        marker = 2
          
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self.dfs(i, j, marker)
                    marker += 1

        largest = 0

        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    visited = set()
                    area = 1
                    for k in range(4):
                        x, y = i + self.dr[k], j + self.dc[k]

                        if 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] > 1:
                            if grid[x][y] not in visited:
                                area += self.areas[grid[x][y]]
                                visited.add(grid[x][y])
                                
                    largest = max(largest, area)
                
        return largest if largest != 0 else self.m * self.n

    def dfs(self, row, col, marker):
            self.grid[row][col] = marker
            self.areas[marker] += 1
            for k in range(4):
                x, y = row + self.dr[k], col + self.dc[k]

                if 0 <= x < self.m and 0 <= y < self.n and self.grid[x][y] == 1:
                    self.dfs(x, y, marker)



    