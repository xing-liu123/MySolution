import heapq
class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []
        self.numCounts = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minHeap, val)
        self.numCounts[val] = self.numCounts.get(val, 0) + 1

    def pop(self) -> None:
        if not self.stack:
            return
        
        val = self.stack.pop()
        self.numCounts[val] -= 1

        if val == self.minHeap[0]:
            heapq.heappop(self.minHeap)

    def top(self) -> int:
        if not self.stack:
            return None
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minHeap:
            return None

        while self.minHeap and self.numCounts.get(self.minHeap[0]) == 0:
            heapq.heappop(self.minHeap)

        if self.minHeap:
            return self.minHeap[0]
        else:
            return None
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()