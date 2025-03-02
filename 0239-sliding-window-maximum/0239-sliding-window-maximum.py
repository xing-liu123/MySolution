class MaxQueue:
    def __init__(self):
        self.queue = []

    def enque(self, val):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()

        self.queue.append(val)

    def remove(self, val):
        if val == self.queue[0]:
            self.queue = self.queue[1:]

    def getMax(self):
        if len(self.queue) > 0:
            return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MaxQueue()

        res = []

        for idx, num in enumerate(nums):
            queue.enque(num)

            if idx >= k:
                queue.remove(nums[idx - k])

            if idx >= k - 1:
                res.append(queue.getMax())

        return res
            