class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_sign = "+"

        for idx, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c in "+-*/" or idx == len(s) - 1:
                if last_sign == "+":
                    stack.append(num)
                elif last_sign == "-":
                    stack.append(-num)
                elif last_sign == "*":
                    stack.append(stack.pop() * num)
                elif last_sign == "/":
                    stack.append(int(stack.pop() / num))
                
                num = 0
                last_sign = c

        return sum(stack)