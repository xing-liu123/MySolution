class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # path = [""] * (2 * n)
        # res = []

        # def generate(idx, open_count, close_count):
        #     if idx == 2 * n:
        #         res.append("".join(path))
        #         return

        #     if open_count < n:
        #         path[idx] = "("
        #         generate(idx + 1, open_count + 1, close_count)

        #     if close_count < open_count:
        #         path[idx] = ")"
        #         generate(idx + 1, open_count, close_count + 1)
        
        # generate(0, 0, 0)

        # return res

        comb = [""] * (n * 2)

        res = []

        def generate(idx, openCount, closeCount):
            if idx == 2 * n:
                res.append("".join(comb))
                return

            if openCount < n:
                comb[idx] = "("
                generate(idx + 1, openCount + 1, closeCount)
            
            if closeCount < openCount:
                comb[idx] = ")"
                generate(idx + 1, openCount, closeCount + 1)

        generate(0, 0, 0)

        return res