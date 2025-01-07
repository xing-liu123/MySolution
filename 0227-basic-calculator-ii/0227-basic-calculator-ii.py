class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        s = s.replace(" ", "")

        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                    print(stack)
                
                num = 0
                sign = c
            
        return sum(stack)