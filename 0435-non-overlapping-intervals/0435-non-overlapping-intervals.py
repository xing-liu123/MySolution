class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        lastInterval = intervals[0][1]
        for i in range(1, len(intervals)):

            if intervals[i][0] < lastInterval:
                count+=1
            else:
                lastInterval = intervals[i][1]

        return count