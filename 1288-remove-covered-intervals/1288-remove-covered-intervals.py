class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        removeCount = 0
        currentRightBorder = intervals[0][1]

        for _, right in intervals[1:]:
            if currentRightBorder >= right:
                removeCount += 1
            else:
                currentRightBorder = right

        return len(intervals) - removeCount
