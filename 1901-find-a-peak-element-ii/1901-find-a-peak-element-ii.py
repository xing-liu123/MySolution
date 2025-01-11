class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        left = 0
        right = m - 1

        def findMaxCol(row):
            max_col = 0

            for col in range(1, n):
                if mat[row][col] > mat[row][max_col]:
                    max_col = col

            return max_col

        while left <= right:
            mid = (left + right) // 2

            max_col = findMaxCol(mid)

            if (mid == 0 or mat[mid][max_col] > mat[mid - 1][max_col]) and (mid == m - 1 or mat[mid][max_col] > mat[mid + 1][max_col]):
                return [mid, max_col]

            if mid > 0 and mat[mid][max_col] <= mat[mid - 1][max_col]:
                right = mid - 1
            else:
                left = mid + 1

