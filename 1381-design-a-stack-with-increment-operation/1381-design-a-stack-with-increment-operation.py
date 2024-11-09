class CustomStack:

    def __init__(self, maxSize: int):
        self.array = [0] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < len(self.array):
            self.array[self.size] = x
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        
        self.size -= 1
        return self.array[self.size]

    def increment(self, k: int, val: int) -> None:
        k = min(k, self.size)

        for i in range(k):
            self.array[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)