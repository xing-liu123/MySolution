class Solution:
    def __init__(self):
        self.subset = []
        self.result = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtracking(nums, 0)
        return self.result
        
    def backtracking(self, nums: int, start: int):
        if len(self.subset) > 1:
            self.result.append(copy.copy(self.subset))

        used = set()
        for i in range(start, len(nums)):
            if nums[i] in used:
                continue

            if not self.subset or nums[i] >= self.subset[-1]:
                used.add(nums[i])
                self.subset.append(nums[i])
                self.backtracking(nums, i + 1)
                self.subset.pop()