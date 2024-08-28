class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numOfDigitLow = len(str(low))
        numOfDigitHigh = len(str(high))

        num = "123456789"

        length = numOfDigitLow
        i = 0

        res = []

        while True:
            if i + length > 9:
                i = 0
                length += 1
            
            if length > numOfDigitHigh or length > 9:
                break

            s = num[i: i + length]
            if low <= int(s) <= high:
                res.append(int(s))
            
            i += 1

        return res
