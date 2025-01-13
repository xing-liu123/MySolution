from bisect import bisect_left, bisect_right
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
       # Find the correct position to insert the new interval
        idx = bisect_left(self.bookings, (startTime, endTime))
        
        # Check overlap with the previous interval
        if idx > 0 and self.bookings[idx - 1][1] > startTime:
            return False
        
        # Check overlap with the next interval
        if idx < len(self.bookings) and self.bookings[idx][0] < endTime:
            return False
        
        # No overlaps, insert the interval
        self.bookings.insert(idx, (startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)