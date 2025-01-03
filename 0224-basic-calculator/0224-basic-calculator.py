class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Stack to handle parentheses and intermediate results
        current_number = 0  # Current number being processed
        current_sign = 1  # Current sign: +1 for positive, -1 for negative
        result = 0  # Cumulative result

        for char in s:
            if char.isdigit():
                # Build the current number
                current_number = current_number * 10 + int(char)
            elif char == '+':
                # Apply the current number and reset
                result += current_sign * current_number
                current_number = 0
                current_sign = 1  # Update to positive sign
            elif char == '-':
                # Apply the current number and reset
                result += current_sign * current_number
                current_number = 0
                current_sign = -1  # Update to negative sign
            elif char == '(':
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(current_sign)
                # Reset result and sign for the new subexpression
                result = 0
                current_sign = 1
            elif char == ')':
                # Apply the current number to the result
                result += current_sign * current_number
                current_number = 0
                # Pop the sign and previous result from the stack
                current_sign = stack.pop()
                result = stack.pop() + current_sign * result

        # Apply the last number in the string
        result += current_sign * current_number
        return result

        