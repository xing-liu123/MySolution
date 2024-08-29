class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        chars = list(s)
        n = len(chars)

        
        for i in range(n):
            c = chars[i]
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = "."
                
        if stack:
            stack = []

            for i in range(n - 1, -1, -1):
                c = chars[i]

                if c == ")":
                    stack.append(c)
                elif c == "(":
                    if stack:
                        stack.pop()
                    else:
                        chars[i] = "."

        res = ""

        for c in chars:
            if c != ".":
                res += c
        
        return res