class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = []
        self.k = k
        
        for num in nums:
            heapq.heappush(self.queue, num)

            if len(self.queue) > k:
                heapq.heappop(self.queue)

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)

        if len(self.queue) > self.k:
            heapq.heappop(self.queue)
        
        return self.queue[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)