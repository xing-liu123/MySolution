class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        counts = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                counts[i] = counts[i - 1] + 1
            else:
                counts[i] = 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                counts[i] = max(counts[i + 1] + 1, counts[i])

        return sum(counts)
