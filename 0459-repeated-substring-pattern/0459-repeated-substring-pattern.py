class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        table = [0] * len(s)
        
        i, j = 0, 1
        
        while j < len(s):
            if s[i] == s[j]:
                table[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = table[i - 1]
        
        return len(s) % (len(s) - table[-1]) == 0 and table[-1] != 0
        