from collections import deque
class MyQueue:

    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        while self.queue and self.queue[-1] < x:
            self.queue.pop()

        self.queue.append(x)

    def front(self):
        return self.queue[0]
    

    def pop(self, x):
        if self.queue and x == self.queue[0]:
            self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()

        res = []

        for idx, num in enumerate(nums):
            queue.push(num)

            if idx >= k:
                queue.pop(nums[idx - k])

            if idx >= k - 1:
                res.append(queue.front())

            
        return res

