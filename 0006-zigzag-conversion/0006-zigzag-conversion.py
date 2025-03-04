class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        numCols = (len(s) + (numRows) - 1) // numRows

        rows = [""] * numRows

        idx = 0
        row, col = 0, 0

        while idx < len(s):
            rows[row] += s[idx]
            idx += 1

            if col % (numRows - 1) == 0:
                if row == numRows - 1:
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                row -= 1
                col += 1
        
        return ''.join(rows)
