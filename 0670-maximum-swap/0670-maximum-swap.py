class Solution:
    def maximumSwap(self, num: int) -> int:
        idxCouldSwap = -1

        for idx in range(1, len(str(num))):
            if str(num)[idx] > str(num)[idx - 1]:
                idxCouldSwap = idx - 1
                break

        if idxCouldSwap == -1:
            return num

        currMaxIdx = idxCouldSwap + 1

        for idx in range(idxCouldSwap + 2, len(str(num))):
            if str(num)[idx] >= str(num)[currMaxIdx]:
                currMaxIdx = idx

        idxToSwap = idxCouldSwap
        for idx in range(idxCouldSwap + 1):
            if str(num)[idx] < str(num)[currMaxIdx]:
                idxToSwap = idx
                break

        res = 0
        mul = 1

        for idx in range(len(str(num)) - 1, -1, -1):
            if idx == currMaxIdx:
                res += int(str(num)[idxToSwap]) * mul
            elif idx == idxToSwap:
                res += int(str(num)[currMaxIdx]) * mul
            else:
                res += int(str(num)[idx]) * mul
            
            mul *= 10

        return res