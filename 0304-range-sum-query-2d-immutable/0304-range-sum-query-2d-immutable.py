class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])

        self.rowPrefixSum = [row[:] for row in matrix]
        self.colPrefixSum = [row[:] for row in matrix]

        for i in range(self.m):
            for j in range(1, self.n):
                self.rowPrefixSum[i][j] += self.rowPrefixSum[i][j - 1]
        
        for j in range(self.n):
            for i in range(1, self.m):
                self.colPrefixSum[i][j] += self.colPrefixSum[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row2 - row1 < col2 - col1:
            res = 0
            for i in range(row1, row2 + 1):
                res += self.rowPrefixSum[i][col2]
                if col1 != 0:
                    res -= self.rowPrefixSum[i][col1 - 1]
        else:
            res = 0
            for j in range(col1, col2 + 1):
                res += self.colPrefixSum[row2][j]
                if row1 != 0:
                    res -= self.colPrefixSum[row1 - 1][j]
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)