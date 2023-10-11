class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        maxValue = 2**31 - 1
        minValue = -2**31

        while x != 0:
            digit = int(math.fmod(x, 10)) 
            
            if res > maxValue // 10 or (res == maxValue // 10 and digit > maxValue % 10):
                return 0
            
            if res < minValue // 10 or (res == minValue // 10 and digit < minValue % 10):
                return 0
            
            res = res * 10 + digit
            x = int(x / 10)

        return res