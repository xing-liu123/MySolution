class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for c in s:
            if c.islower():
                stack.append(c)
            else:
                if not stack:
                    stack.append(c)
                else:
                    stack.pop()
        
        return ''.join(stack)