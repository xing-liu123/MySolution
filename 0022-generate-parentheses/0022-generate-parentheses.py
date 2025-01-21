class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = [""] * (2 * n)
        res = []

        def generate(idx, open_count, close_count):
            if idx == 2 * n:
                res.append("".join(path))
                return

            if open_count < n:
                path[idx] = "("
                generate(idx + 1, open_count + 1, close_count)
                path[idx] = ""

            if close_count < open_count:
                path[idx] = ")"
                generate(idx + 1, open_count, close_count + 1)
                path[idx] = ""
        
        generate(0, 0, 0)

        return res