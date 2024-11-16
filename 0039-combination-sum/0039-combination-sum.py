class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.res
    
    def backtracking(self, candidates: List[int], target: int, start: int, currSum: int):
        if currSum == target:
            self.res.append(copy.copy(self.path))
            return
        
        for i in range(start, len(candidates)):
            if currSum + candidates[i] > target:
                return
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i, currSum + candidates[i])
            self.path.pop()
