class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

        for i in range(self.m):
            for j in range(1, self.n):
                self.matrix[i][j] += self.matrix[i][j - 1]
    

        for i in range(1, self.m):
            for j in range(self.n):
                self.matrix[i][j] += self.matrix[i - 1][j] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix[row2][col2]

        if row1 > 0:
            res -= self.matrix[row1 - 1][col2]
        
        if col1 > 0:
            res -= self.matrix[row2][col1 - 1]

        if col1 > 0 and row1 > 0:
            res += self.matrix[row1 - 1][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)