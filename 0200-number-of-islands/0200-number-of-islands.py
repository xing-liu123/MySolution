class Solution:
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        
        return count
    
    def dfs(self, grid: List[List[str]], row:int, col:int):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
            return
            
        grid[row][col] = "0"

        for i in range(4):
            self.dfs(grid, row + self.dr[i], col + self.dc[i])