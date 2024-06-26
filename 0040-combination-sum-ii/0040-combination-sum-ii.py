class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        
        if candidates[0] > target:
            return res
        
        def backtracking(start, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] + curr_sum > target:
                    return
                
                path.append(candidates[i])
                backtracking(i + 1, curr_sum + candidates[i])
                path.pop()
        
        backtracking(0, 0)
        
        return res
            