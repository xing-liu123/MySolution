from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif (len(self.minHeap) != 0 and -self.maxHeap[0] > self.minHeap[0]):
            valInMax = -heappop(self.maxHeap)
            valInMin = -heappop(self.minHeap)
            heappush(self.maxHeap, valInMin)
            heappush(self.minHeap, valInMax)


    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()