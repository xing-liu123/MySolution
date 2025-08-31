from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        strN = str(n)
        counts = Counter(strN)

        curr = 1

        while len(str(curr)) <= len(strN):
            currCounts = Counter(str(curr))

            if counts == currCounts:
                return True

            curr *= 2

        return False


