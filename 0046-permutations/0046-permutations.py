class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.used = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [0] * len(nums)
        self.backtracking(nums)
        return self.res
    
    def backtracking(self, nums: List[int]):
        if len(self.path) == len(nums):
            self.res.append(copy.copy(self.path))
        
        for i in range(len(nums)):
            if self.used[i]:
                continue
            
            self.path.append(nums[i])
            self.used[i] = 1
            self.backtracking(nums)
            self.path.pop()
            self.used[i] = 0
