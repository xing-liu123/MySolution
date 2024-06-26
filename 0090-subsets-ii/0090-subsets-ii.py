class Solution:
    

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        
        nums.sort()
        
        def backtracking(start):
            res.append(path.copy())
            
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                    
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
                
        backtracking(0)
        
        return res


