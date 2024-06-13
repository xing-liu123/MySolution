from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()
        
    def push(self, val: int):
        while self.queue and val > self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)
        
    def pop(self, val: int):
        if self.queue and val == self.queue[0]:
            self.queue.popleft()
    
    def front(self) -> int:
        return self.queue[0]
        
class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        myQ = MyQueue()
        res = []
        for i in range(k):
            myQ.push(nums[i])
        
        res.append(myQ.front())
        
        for i in range(k, len(nums)):
            myQ.pop(nums[i - k])
            myQ.push(nums[i])
            res.append(myQ.front())
        
        return res