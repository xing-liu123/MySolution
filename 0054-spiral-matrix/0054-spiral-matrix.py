class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        m, n = len(matrix), len(matrix[0])

        size = m * n
        row, col = 0, 0
        direction = 0 if n > 1 else 1 # 0: right, 1: down, 2: left, 3: right
        top, left, bottom, right = 1, 0, m - 1, n - 1

        while len(res) < size:
            print(row, col)
            res.append(matrix[row][col])

            if direction == 0:
                col += 1

                if col == right:
                    direction = 1
                    right -= 1

            elif direction == 1:
                row += 1

                if row == bottom:
                    direction = 2
                    bottom -= 1

            elif direction == 2:
                col -= 1

                if col == left:
                    direction = 3
                    left += 1
            else:
                row -= 1

                if row == top:
                    direction = 0
                    top += 1

        return res

