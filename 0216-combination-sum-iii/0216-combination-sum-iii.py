class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(1, 0, k, n)
        return self.res

    def backtracking(self, curr, currSum, k, n):
        if len(self.path) == k:
            if currSum == n:
                self.res.append(copy.copy(self.path))

            return

        for i in range(curr, 10):
            if currSum + i > n:
                return
            
            self.path.append(i)
            self.backtracking(i + 1, currSum + i, k, n)
            self.path.pop()


            