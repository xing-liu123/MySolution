class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        while num > 0:
            if num >= 1000:
                count = num // 1000
                res += "M" * count
                num %= 1000
            elif num >= 900:
                res += "CM"
                num %= 900
            elif num >= 500:
                res += "D"
                num -= 500
            elif num >= 400:
                res += "CD"
                num %= 400
            elif num >= 100:
                count = num // 100
                res += "C" * count
                num %= 100
            elif num >= 90:
                res += "XC"
                num %= 90
            elif num >= 50:
                res += "L"
                num -= 50
            elif num >= 40:
                res += "XL"
                num %= 40
            elif num >= 10:
                count = num // 10
                res += "X" * count
                num %= 10
            elif num == 9:
                res += "IX"
                num = 0
            elif num >= 5:
                res += "V"
                num -= 5
            elif num == 4:
                res += "IV"
                num = 0
            elif num >= 1:
                res += "I" * num
                num = 0
        return res