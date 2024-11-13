class MyQueue:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        

    def push(self, x: int) -> None:
        while self.stackB:
            self.stackA.append(self.stackB.pop())
        self.stackA.append(x)

    def pop(self) -> int:
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

    def peek(self) -> int:
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        return self.stackB[-1]
        

    def empty(self) -> bool:
        return not self.stackA and not self.stackB


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()