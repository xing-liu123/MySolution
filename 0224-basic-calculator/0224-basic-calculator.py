class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        current_sign = 1
        result = 0

        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c == "+":
                result = result + current_sign * current_num
                current_num = 0
                current_sign = 1
            elif c == "-":
                result = result + current_sign * current_num
                current_num = 0
                current_sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(current_sign)
                result = 0
                current_sign = 1
            elif c == ")":
                result = result + current_sign * current_num
                current_num = 0
                current_sign = stack.pop()
                result = stack.pop() + current_sign * result

        result += current_sign * current_num

        return result
            

            

        