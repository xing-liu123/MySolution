from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, val):
        if not self.queue:
            self.queue.append(val)
        else:
            while self.queue and val > self.queue[-1]:
                self.queue.pop()

            self.queue.append(val)
    
    def remove(self, val):
        if self.queue[0] == val:
            self.queue.popleft()

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()
        res = []

        for i in range(len(nums)):
            queue.push(nums[i])

            if i >= k:
                queue.remove(nums[i - k])

            if i >= k - 1:
                res.append(queue.front())

        return res
            
            

