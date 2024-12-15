class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.array = []
        self.flatten(vec)
        self.size = len(self.array)
        self.index = 0
    
    def flatten(self, vec):
        for v in vec:
            if isinstance(v, list):
                self.flatten(v)
            else:
                self.array.append(v)


    def next(self) -> int:
        val = self.array[self.index]
        self.index += 1

        return val

    def hasNext(self) -> bool:
        return self.index < self.size
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()