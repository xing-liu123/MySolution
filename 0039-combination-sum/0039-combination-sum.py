class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combination = []
        res = []

        if candidates[0] > target:
            return res

        def backtracking(idx, currSum):
            if currSum == target:
                res.append(copy.copy(combination))
                return

            for i in range(idx, len(candidates)):
                if currSum + candidates[i] <= target:
                    combination.append(candidates[i])
                    backtracking(i, currSum + candidates[i])
                    combination.pop()
                else:
                    break

        backtracking(0, 0)
        return res


