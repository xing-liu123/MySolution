class Solution:
    def __init__(self):
        self.path = ""
        self.res = []
        self.map = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]] 


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.res
            
        self.backtracking(digits, 0)
        return self.res
    
    def backtracking(self, digits: str, idx: int):
        if idx == len(digits):
            self.res.append(copy.copy(self.path))
            return


        for d in self.map[int(digits[idx]) - 2]:
            self.path += d
            self.backtracking(digits, idx + 1)
            self.path = self.path[:len(self.path) - 1]