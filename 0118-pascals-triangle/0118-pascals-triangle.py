class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]

        row = 3
        while row <= numRows:
            curr = [0] * row
            curr[0] = 1
            curr[-1] = 1

            for i in range(1, row - 1):
                curr[i] = res[-1][i - 1] + res[-1][i]
            
            res.append(curr)
            row += 1

        return res
        

