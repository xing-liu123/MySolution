class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, 0)
        return self.res

    def backtracking(self, nums: List[int], start: int):
        
        self.res.append(copy.copy(self.path))
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
