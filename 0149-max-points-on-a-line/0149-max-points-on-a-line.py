class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        lineCounts = defaultdict(set)

        for i in range(n):
            for j in range(i + 1, n):
                k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) if (points[i][0] - points[j][0]) != 0 else float("inf")
                b = (points[i][1] - k * points[i][0]) if k != float("inf") else points[i][0]

                lineCounts[(k, b)].add((points[i][0], points[i][1]))
                lineCounts[(k, b)].add((points[j][0], points[j][1]))

        


        if len(lineCounts) == 0:
            return 1

        return max(len(line) for line in lineCounts.values())