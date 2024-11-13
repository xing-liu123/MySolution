class Solution:
    def isHappy(self, n: int) -> bool:

        numSet = set()

        while True:
            if n == 1:
                return True

            if n in numSet:
                return False
            
            numSet.add(n)

            

            n = sum(int(digit) ** 2 for digit in str(n))

        return False
