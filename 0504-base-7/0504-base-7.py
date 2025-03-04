class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        isNegative = num < 0
        num = abs(num)

        ans = ""

        while num > 0:
            res = num % 7
            num //= 7

            ans = str(res) + ans


        if isNegative:
            ans = "-" + ans

        return ans