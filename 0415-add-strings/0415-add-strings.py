class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = 0

        idx1, idx2 = len(num1) - 1, len(num2) - 1
        base = 1
        carry = 0

        while idx1 >= 0 or idx2 >= 0:
            currSum = carry

            if idx1 >= 0:
                currSum += int(num1[idx1])
                idx1 -= 1

            if idx2 >= 0:
                currSum += int(num2[idx2])
                idx2 -= 1
            
            res += (currSum % 10) * base
            carry = currSum // 10
            base *= 10
        
        res += carry * base

        return str(res)