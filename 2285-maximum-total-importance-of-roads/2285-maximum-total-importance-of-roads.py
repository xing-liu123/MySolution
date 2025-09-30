class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n

        for start, end in roads:
            degrees[start] += 1
            degrees[end] += 1

        degrees.sort()

        return sum((i + 1) * degrees[i] for i in range(n))