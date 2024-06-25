class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        
        def backtracking(k, n, start, curr_sum):            
            if len(path) == k:
                if curr_sum == n:
                    res.append(path.copy())
                
                return
            
            for i in range(start, 10):
                if curr_sum + i > n:
                    return
                
                path.append(i)
                backtracking(k, n, i + 1, curr_sum + i)
                path.pop()
        
        backtracking(k, n, 1, 0)
        
        return res
        
            