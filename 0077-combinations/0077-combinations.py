class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(1, k, n)
        return self.res

    def backtracking(self, start, k, n):
        if len(self.path) == k:
            self.res.append(copy.copy(self.path))
            return

        for i in range(start, n - (k - len(self.path)) + 2): # k - len(self.path)
            self.path.append(i)
            self.backtracking(i + 1, k, n)
            self.path.pop()
    