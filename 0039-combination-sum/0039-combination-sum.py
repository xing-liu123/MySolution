class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.sum = 0
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.res
    
    def backtracking(self, candidates: List[int], target: int, start: int):
        if self.sum == target:
            self.res.append(copy.copy(self.path))
            return
        
        for i in range(start, len(candidates)):
            if self.sum + candidates[i] > target:
                return
            self.path.append(candidates[i])
            self.sum += candidates[i]
            self.backtracking(candidates, target, i)
            self.path.pop()
            self.sum -= candidates[i]