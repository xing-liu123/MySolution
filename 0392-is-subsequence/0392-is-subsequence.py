class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = 0, 0

        while m < len(s) and n < len(t):
            if s[m] == t[n]:
                m += 1

            n += 1
        
        return m == len(s)
