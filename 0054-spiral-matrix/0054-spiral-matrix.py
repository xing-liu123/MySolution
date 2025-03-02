class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        m, n = len(matrix), len(matrix[0])
        row, col = 0, 0

        top, bottom, left, right = 1, m - 1, 0, n - 1
        currDir = 0 if n > 1 else 1 # 0: right, 1: down, 2: left, 3: up

        for _ in range(m * n):
            res.append(matrix[row][col])

            match currDir:
                case 0:
                    col += 1
                    if col == right:
                        currDir = 1
                        right -= 1

                case 1:
                    row += 1
                    if row == bottom:
                        currDir = 2
                        bottom -= 1
                case 2:
                    col -= 1
                    if col == left:
                        currDir = 3
                        left += 1
                case 3:
                    row -= 1
                    if row == top:
                        currDir = 0
                        top += 1

        return res
