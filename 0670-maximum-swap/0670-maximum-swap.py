class Solution:
    def maximumSwap(self, num: int) -> int:
        numList = list(str(num))
        lastOccurrence = {int(x): i for i, x in enumerate(numList)}

        for i, d in enumerate(numList):
            for x in range(9, int(d), -1):
                if lastOccurrence.get(x, -1) > i:
                    numList[i], numList[lastOccurrence[x]] = numList[lastOccurrence[x]], numList[i]
                    return int(''.join(numList))

        return num