class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        partLen = len(part)
        partList = list(part)

        for c in s:
            stack.append(c)

            if len(stack) >= len(part) and stack[-partLen:] == partList:
                stack = stack[:-partLen]
            
        return "".join(stack)


        

