class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.used = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.used = [0] * len(nums)
        nums.sort()
        self.backtracking(nums)
        return self.res
    
    def backtracking(self, nums: List[int]):
        if len(self.path) == len(nums):
            self.res.append(copy.copy(self.path))
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and self.used[i - 1] == 0:
                continue

            if self.used[i] == 0:
                self.used[i] = 1
                self.path.append(nums[i])
                self.backtracking(nums)
                self.used[i] = 0
                self.path.pop()