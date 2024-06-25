class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()
        
        def backtracking(start, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                    
                if curr_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtracking(i, candidates[i] + curr_sum)
                path.pop()
        
        backtracking(0, 0)
        
        return res