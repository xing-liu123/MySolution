class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        zeroCount = binary.count('0')
        oneCount = len(binary) - zeroCount

        return zeroCount + (1 + (oneCount - 1) * 2)