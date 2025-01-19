class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if len(derived) == 1:
            return derived[0] == 0

        def isValid(prev, curr):
            start = prev

            for i in range(1, len(derived) - 1):
                if derived[i] == 0:
                    prev, curr = curr, curr
                else:
                    prev, curr = curr, 1 - curr

            if derived[-1] == 1:
                return start != curr
            else:
                return start == curr

        if derived[0] == 1:
            return isValid(1, 0) or isValid(0, 1)
        else:
            return isValid(0, 0) or isValid(1, 1)