class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 + val2)
            elif token == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif token == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 * val2)
            elif token == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                res = val1 / val2

                if res >= 0:
                    res = math.floor(res)
                else:
                    res = math.ceil(res)
                stack.append(res)

            else: 
                stack.append(int(token))

        return stack.pop()