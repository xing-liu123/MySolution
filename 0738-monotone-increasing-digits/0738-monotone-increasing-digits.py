class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n

        num = list(str(n))
        marker = len(num)
        
        for i in range(len(num) - 1, 0, -1):
            if num[i] < num[i - 1]:
                num[i - 1] = str(int(num[i - 1]) - 1)
                marker = i

        for i in range(marker, len(num)):
            num[i] = '9'

        return int(''.join(num))