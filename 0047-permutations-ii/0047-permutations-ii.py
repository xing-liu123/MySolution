class Solution:
   

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False] * len(nums)
        nums.sort()

        def backtracking():
            if len(path) == len(nums):
                res.append(copy.copy(path))
                return
            
            for i in range(len(nums)):
                if not used[i] and (i == 0 or i > 0 and nums[i] != nums[i - 1] or used[i - 1]):
                    path.append(nums[i])
                    used[i] = True
                    backtracking()
                    used[i] = False
                    path.pop()

        backtracking()
        return res