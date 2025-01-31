class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            return 0

        def distributeWithoutLimit(n, k):
            if n < 0:
                return 0

            return math.comb(n + k - 1, k - 1)

        totalCount = distributeWithoutLimit(n, 3)

        totalCount -= 3 * distributeWithoutLimit(n - (limit + 1), 3)
        totalCount += 3 * distributeWithoutLimit(n - (limit + 1) * 2, 3)

        return totalCount