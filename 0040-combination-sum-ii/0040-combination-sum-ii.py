class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.res
    
    def backtracking(self, candidates: List[int], target: int, start: int):
        if self.sum == target:
            self.res.append(copy.copy(self.path))
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            if self.sum + candidates[i] > target:
                break
            
            self.sum += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i + 1)
            self.path.pop()
            self.sum -= candidates[i]