class Node:
    def __init__(self, val: int, min: int):
        self.val = val
        self.min = min

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Node(val, val))
        else:
            self.stack.append(Node(val, min(val, self.stack[-1].min)))

    def pop(self) -> None:
        if not self.stack:
            return
       
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        
        return self.stack[-1].val     

    def getMin(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1].min
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()