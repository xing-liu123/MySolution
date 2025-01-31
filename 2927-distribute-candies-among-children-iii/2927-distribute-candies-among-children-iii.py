class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            return 0

        def Combinatorics(n, k):
            if n < 0:
                return 0

            return math.comb(n + k - 1, k - 1)

        totalCount = Combinatorics(n, 3)

        totalCount -= 3 * Combinatorics(n - (limit + 1), 3)
        totalCount += 3 * Combinatorics(n - 2 * (limit + 1), 3)

        return totalCount