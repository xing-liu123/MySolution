class Solution:
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    def __init__(self):
        self.res = 0
        self.currMax = 0
        


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    self.currMax = 0
                    self.dfs(grid, i, j) 
        
        return self.res
    
    def dfs(self, grid: List[List[int]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        self.currMax += 1
        self.res = max(self.res, self.currMax)

        for k in range(4):
            self.dfs(grid, i + self.dr[k], j + self.dc[k]) 