from collections import deque
class HitCounter:

    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        # Check if the queue has hits recorded for the same timestamp
        if self.queue and self.queue[-1][0] == timestamp:
            # Update the count for the last recorded timestamp
            self.queue[-1][1] += 1
        else:
            # Append a new timestamp with count 1
            self.queue.append([timestamp, 1])
        

    def getHits(self, timestamp: int) -> int:
        # Remove timestamps older than 300 seconds from the current timestamp
        while self.queue and self.queue[0][0] <= timestamp - 300:
            self.queue.popleft()
        
        # Sum the counts of the remaining timestamps in the window
        return sum(count for _, count in self.queue)

            



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)