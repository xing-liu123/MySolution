import queue
class MyStack:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.topElement = None

    def push(self, x: int) -> None:
        self.q1.put(x)
        self.topElement = x

    def pop(self) -> int:
        while self.q1.qsize() > 1:
            self.topElement = self.q1.get()
            self.q2.put(self.topElement)
        
        res = self.q1.get()
        
        self.q1, self.q2 = self.q2, self.q1
        
        return res

    def top(self) -> int:
        return self.topElement

    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()