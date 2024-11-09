from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        if self.queue:
            _, count = self.queue[-1]
            self.queue.append((timestamp, count + 1))
        else:
            self.queue.append((timestamp, 1))
        

    def getHits(self, timestamp: int) -> int:
        if not self.queue:
            return 0
        else:
            if self.queue[-1][0] + 300 <= timestamp:
                self.queue = deque()
                return 0
            
            while len(self.queue) >= 2 and self.queue[1][0] + 300 <= timestamp:
                self.queue.popleft()

            if len(self.queue) == 1:
                return self.queue[0][1]
            elif self.queue[0][0] + 300 > timestamp:
                return self.queue[-1][1]
            else:
                return self.queue[-1][1] - self.queue[0][1]

            



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)