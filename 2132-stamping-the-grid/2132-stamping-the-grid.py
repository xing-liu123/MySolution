class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = grid[i][j] - prefix[i][j] + prefix[i + 1][j] + prefix[i][j + 1]

        def hasOccupiedCells(x1, x2, y1, y2):
            return prefix[x2 + 1][y2 + 1] + prefix[x1][y1] - prefix[x2 + 1][y1] - prefix[x1][y2 + 1] > 0

        stampable = [[0] * n for _ in range(m)]

        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                if grid[i][j] != 1:
                    if not hasOccupiedCells(i, i + stampHeight - 1, j, j + stampWidth - 1):
                        stampable[i][j] = 1

        diff = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                if stampable[i][j] == 1:
                    diff[i][j] += 1
                    diff[i + stampHeight][j] -= 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1

        stamped = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]

                if j > 0:
                    diff[i][j] += diff[i][j - 1]

                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]

                stamped[i][j] = 1 if diff[i][j] > 0 else 0


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and stamped[i][j] == 0:
                    return False

        return True

