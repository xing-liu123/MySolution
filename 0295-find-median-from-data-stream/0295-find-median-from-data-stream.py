class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap and not self.minHeap:
            heapq.heappush(self.maxHeap, -num)
            return
        elif not self.minHeap:
            if -self.maxHeap[0] <= num:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)
        elif not self.maxHeap:
            if self.minHeap[0] >= num:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
        else:
            if (len(self.maxHeap) + len(self.minHeap)) % 2 == 1:
                if num >= -self.maxHeap[0]:
                    heapq.heappush(self.minHeap, num)
                else:
                    heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                    heapq.heappush(self.maxHeap, -num)
            else:
                if num <= self.minHeap[0]:
                    heapq.heappush(self.maxHeap, -num)
                else:
                    heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                    heapq.heappush(self.minHeap, num)
        
        
        


    def findMedian(self) -> float:
        if len(self.maxHeap) + len(self.minHeap) == 0:
            return None
        elif (len(self.maxHeap) + len(self.minHeap)) % 2 == 1:
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()