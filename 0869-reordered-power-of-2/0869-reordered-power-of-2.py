from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        strN = sorted(str(n))

        curr = 1

        while len(str(curr)) <= len(strN):
            currStr = sorted(str(curr))

            if strN == currStr:
                return True

            curr *= 2

        return False


