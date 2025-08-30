class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0 or n != 1 and n % 2 == 1:
            return False

        return bin(n).count('1') == 1
        
