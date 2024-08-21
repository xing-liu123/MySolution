class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        prefixSums = [[grid[0][0]], [grid[1][0]]]

        for i in range(2):
            for num in grid[i][1:]:
                prefixSums[i].append(prefixSums[i][-1] + num)

        minPoints = sys.maxsize

        for i in range(n):
            currMax = max(prefixSums[0][-1] - prefixSums[0][i], prefixSums[1][i - 1]) if i > 0 else prefixSums[0][-1] - prefixSums[0][i]
            minPoints = min(minPoints, currMax)
        
        return minPoints
                
