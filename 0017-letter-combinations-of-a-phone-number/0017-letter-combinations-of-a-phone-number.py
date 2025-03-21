class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # path = []
        # res = []
        # if len(digits) == 0:
        #     return res

        # key_map = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]] 

        # def backtrack(idx):
        #     if len(path) == len(digits):
        #         res.append(''.join(path))
        #         return

        #     keys = key_map[ord(digits[idx]) - ord('2')]

        #     for key in keys:
        #         path.append(key)
        #         backtrack(idx + 1)
        #         path.pop()

        # backtrack(0)
        # return res

        if len(digits) == 0:
            return []

        key_map = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

        comb = [""] * len(digits)
        res = []

        def backtracking(idx):
            if idx == len(digits):
                res.append(''.join(comb))
                return

            chars = key_map[ord(digits[idx]) - ord('2')]

            for char in chars:
                comb[idx] = char
                backtracking(idx + 1)

        backtracking(0)

        return res
