class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, 0)
        return self.res
    
    def helper(self, nums: List[int], start: int):
        self.res.append(copy.copy(self.path))

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.helper(nums, i + 1)
            self.path.pop()