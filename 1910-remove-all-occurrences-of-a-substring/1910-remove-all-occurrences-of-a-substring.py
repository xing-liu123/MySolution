class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        partLen = len(part)

        for c in s:
            stack.append(c)

            if len(stack) >= len(part) and ''.join(stack[-partLen:]) == part:
                stack = stack[:-partLen]
            
        return "".join(stack)


        

