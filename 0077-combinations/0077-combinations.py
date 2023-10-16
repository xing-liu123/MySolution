class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k, 1)
        return self.res
    
    def backtrack(self, n: int, k: int, start: int):
        if len(self.path) == k:
            self.res.append(copy.copy(self.path))
            return
        
        for i in range (start, n - (k - len(self.path)) + 2):
            self.path.append(i)
            self.backtrack(n, k, i + 1)
            self.path.pop()
        
