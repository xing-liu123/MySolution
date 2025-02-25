class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        var mergedIntervals: [[Int]] = []

        let sortedIntervals = intervals.sorted{$0[0] < $1[0]}

        for interval in sortedIntervals {
            if mergedIntervals.isEmpty || mergedIntervals[mergedIntervals.count - 1][1] < interval[0] {
                mergedIntervals.append(interval)
            } else {
                mergedIntervals[mergedIntervals.count - 1][1] = max(mergedIntervals[mergedIntervals.count - 1][1], interval[1])
            }
            
        }

        return mergedIntervals
    }
}