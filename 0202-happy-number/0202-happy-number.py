class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        numbers = {n}
        
        while n != 1:
            number = n
            digit_sum = 0
            
            while number > 0:
                digit =  number % 10
                digit_sum += digit * digit
                number //= 10
            
            if digit_sum in numbers:
                return False
            
            numbers.add(digit_sum)
            n = digit_sum
        
        return True
            

