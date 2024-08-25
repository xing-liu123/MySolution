class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        size = 2 ** k

        
        if len(s) - k + 1 < size:
            return False
            
        code_set = set()

        curr = s[:k]
        code_set.add(curr)

        for i in range(k, len(s)):
            curr = curr[1:] + s[i]

            code_set.add(curr)

            if len(code_set) == size:
                return True
            
            if len(s) - i - 1 < size - len(code_set):
                return False

        if len(code_set) == size:
                return True 
        