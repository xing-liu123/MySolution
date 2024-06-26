class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        
        def backtracking(start):
            if len(path) >= 2:
                res.append(path.copy())
            
            if start == len(nums):
                return
            
            used = set()
            for i in range(start, len(nums)):
                    
                if (len(path) == 0 or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtracking(i + 1)
                    path.pop()
                    
        backtracking(0)
        
        return res