class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        coordiates = {}

        for i in range(m):
            for j in range(n):
                coordiates[mat[i][j]] = (i, j)

        rows = [n] * m
        cols = [m] * n

        for i, val in enumerate(arr):
            row, col =  coordiates[val]
            cols[col] -= 1
            rows[row] -= 1

            if cols[col] == 0 or rows[row] == 0:
                return i

        return 