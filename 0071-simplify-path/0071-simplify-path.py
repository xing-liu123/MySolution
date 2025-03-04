class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        # print(stack)
        res = ""
        popCount = 0

        while stack:
            c = stack.pop()

            if c == "":
                continue
            elif c == "..":
                popCount += 1
            elif c == ".":
                continue
            elif popCount > 0:
                popCount -= 1
            else:
                res = "/" + c + res

        return res if res != "" else "/"