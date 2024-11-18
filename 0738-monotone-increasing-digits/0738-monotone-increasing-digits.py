class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n

        num = str(n)
        for i in range(len(num) - 1, 0, -1):
            if int(num[i]) < int(num[i - 1]):
                d = 10 ** (len(num) - i)
                return  self.monotoneIncreasingDigits(n // d * d - 1)
        return n