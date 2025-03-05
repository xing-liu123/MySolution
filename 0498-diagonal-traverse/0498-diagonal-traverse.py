class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        size = m * n

        res = []

        row, col = 0, 0
        state = 1
        
        while len(res) < size:
            res.append(mat[row][col])

            if state == 1:
                if row - 1 < 0 and col + 1 >= n:
                    row += 1
                    state = 2
                elif row - 1 < 0:
                    col += 1
                    state = 2

                elif col + 1 >= n:
                    row += 1
                    state = 2

                else:
                    row -= 1
                    col += 1
            else:
                if row + 1 >= m and col - 1 < 0:
                    col += 1
                    state = 1
                elif row + 1 >= m:
                    col += 1
                    state = 1
                elif col - 1 < 0:
                    row += 1
                    state = 1
                else:
                    col -= 1
                    row += 1
                
        return res


