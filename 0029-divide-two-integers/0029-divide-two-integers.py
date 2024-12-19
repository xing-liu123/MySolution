class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        # Subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp_divisor, num_divisors = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            
            # Subtract the largest shifted divisor and add the count
            dividend -= temp_divisor
            result += num_divisors
        
        # Apply the sign
        if negative:
            result = -result
        
        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, result))
