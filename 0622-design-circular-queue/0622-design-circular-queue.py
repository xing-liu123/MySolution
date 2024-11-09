class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [0] * k
        self.front = 0
        self.back = 0
        self.size = 0 

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.array):
            return False
        
        self.array[self.back] = value
        self.size += 1
        self.back = (self.back + 1) % (len(self.array))
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        self.front = (self.front + 1) % (len(self.array))
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1

        return self.array[self.front]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        
        return self.array[(self.back - 1) % len(self.array)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.array)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()