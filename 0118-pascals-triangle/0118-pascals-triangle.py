class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        res = [[1], [1, 1]]

        for i in range(2, numRows):
            sub = [1] * (i + 1)
            left, right = 1, len(sub) - 2
            while left <= right:
                sub[left] = sub[right] = res[i - 1][left - 1] + res[i - 1][left]
                left += 1
                right -= 1
            res.append(sub)

        return res

