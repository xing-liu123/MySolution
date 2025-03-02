class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = [""] * (n * 2)
        res = []

        def backtracking(idx, openCount, closeCount):
            if idx == 2 * n:
                res.append(''.join(comb))
                return

            if openCount < n:
                comb[idx] = "("
                backtracking(idx + 1, openCount + 1, closeCount)

            if closeCount < openCount:
                comb[idx] = ")"
                backtracking(idx + 1, openCount, closeCount + 1)

        backtracking(0, 0, 0)

        return res
