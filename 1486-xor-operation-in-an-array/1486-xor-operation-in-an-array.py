class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0

        for num in range(start, start + 2 * n, 2):
            res ^= num

        return res