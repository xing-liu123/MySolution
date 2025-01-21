class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []

        def generate(open_count, close_count):
            if open_count == n and close_count == n:
                res.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                generate(open_count + 1, close_count)
                path.pop()

            if close_count < open_count:
                path.append(")")
                generate(open_count, close_count + 1)
                path.pop()
        
        generate(0, 0)

        return res