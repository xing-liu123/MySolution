class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            stack.append(char)
            
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        
        return ''.join(stack)