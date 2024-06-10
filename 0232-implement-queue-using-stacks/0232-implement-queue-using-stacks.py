class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.length = 0

    def push(self, x: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        
        self.s1.append(x)
        self.length += 1

    def pop(self) -> int:
        if self.length < 1:
            return None
        
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.length -= 1
        
        return self.s2.pop()

    def peek(self) -> int:
        if self.length < 1:
            return None
        
        while self.s1:
            self.s2.append(self.s1.pop())
        
        return self.s2[-1]

    def empty(self) -> bool:
        return self.length == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()