class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1]))

        lastEnd = points[0][1]
        count = 1

        for i in range(1, len(points)):
            start, end = points[i]

            if start > lastEnd:
                count += 1
                lastEnd = end
            else:
                points[i][1] = lastEnd

        return count