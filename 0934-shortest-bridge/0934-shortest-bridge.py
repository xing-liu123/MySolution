from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        marker = 2
        step = 0

        def dfs(row, col):
            grid[row][col] = marker

            for k in range(4):
                x = row + dr[k]
                y = col + dc[k]


                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 0:
                        grid[row][col] = 2 * marker
                    if grid[x][y] == 1:
                        dfs(x, y)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    marker += 1

        def bfs(row, col):
            nonlocal step
            queue = deque([(row, col)])
            visited = set()

            while queue:
                size = len(queue)
                
                for _ in range(size):
                    cell = queue.popleft()

                    for k in range(4):
                        x = cell[0] + dr[k]
                        y = cell[1] + dc[k]
                        
                        if 0 <= x < n and 0 <= y < n:
                            if not (x, y) in visited:
                                if grid[x][y] == 0:
                                    visited.add((x, y))
                                    queue.append((x, y))
                                elif grid[x][y] == 6:
                                    return True
                    
                step += 1
                            
            return False
                    
        length = sys.maxsize
         
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 4:
                    step = 0
                    if bfs(i, j):
                        length = min(length, step)

                    

        return length





