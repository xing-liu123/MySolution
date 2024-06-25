class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(n, k, 1)
        return self.res
       
    def backtracking(self, n: int, k: int, start: int):
        if len(self.path) == k:
            self.res.append(self.path.copy())
            return 
        
        for i in range(start, n - (k - len(self.path)) + 2):
            self.path.append(i)
            self.backtracking(n, k, i + 1)
            self.path.pop()
        
