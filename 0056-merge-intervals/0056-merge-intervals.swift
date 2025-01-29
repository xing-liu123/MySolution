class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        var mergedIntervals: [[Int]] = []

        let sortedIntervals = intervals.sorted{$0[0] < $1[0]}

        for interval in sortedIntervals {
            if let lastInterval = mergedIntervals.last, interval[0] <= lastInterval[1] {
                mergedIntervals[mergedIntervals.count - 1][1] = max(lastInterval[1], interval[1])
                    
            } else {
                mergedIntervals.append(interval)
            }
            
        }

        return mergedIntervals
    }
}