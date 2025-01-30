class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit * 3 < n:
            return 0

        def boundedCombinatorics(n: int, k: int):
            if n < 0:
                return 0

            return math.comb(n + k - 1, k - 1)
        
        totalCount = boundedCombinatorics(n, 3)

        totalCount -= 3 * boundedCombinatorics(n - (limit + 1), 3)
        totalCount += 3 * boundedCombinatorics(n - 2 * (limit + 1), 3)


        return totalCount

