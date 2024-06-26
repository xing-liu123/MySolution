class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
    
        def backtracking(start: int):
            res.append(path.copy())
            
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
        
        backtracking(0)
        
        return res