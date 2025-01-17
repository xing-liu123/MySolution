class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False] * len(nums)

        def backtracking():
            if len(path) == len(nums):
                res.append(copy.copy(path))
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtracking()
                    used[i] = False
                    path.pop()

        backtracking()
        return res