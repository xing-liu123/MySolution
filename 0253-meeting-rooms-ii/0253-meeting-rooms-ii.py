class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        n = len(intervals)
        intervals.sort()

        minHeap = []
        heapq.heappush(minHeap, (intervals[0][1]))
        
        for i in range(1, n):
            if intervals[i][0] >= minHeap[0]:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, intervals[i][1])

        return len(minHeap)