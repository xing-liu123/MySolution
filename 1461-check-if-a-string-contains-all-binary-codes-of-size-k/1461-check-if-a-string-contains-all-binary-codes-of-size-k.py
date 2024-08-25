class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        size = 2 ** k

        if len(s) - k + 1 < size:
            return False
            
        code_set = set()


        for i in range(len(s) - k + 1):

            code_set.add(s[i : i + k])

            if len(code_set) == size:
                return True

        return len(code_set) == size
        