class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        idx1, idx2 = 0, 0

        while idx1 < len(s) and idx2 < len(p):
            if s[idx1] == p[idx2] or p[idx2] == ".":
                idx1 += 1
                idx2 += 1
            elif idx1 > 0 and s[idx1] == s[idx1 - 1] and p[idx2] == "*":
                idx1 += 1
            elif idx2 > 0 and p[idx2 - 1] == "." and p[idx2] == "*":
                idx1 += 1
            elif p[idx2] == "*" and idx2 < len(p) - 1 and (p[idx2 + 1] == s[idx1] or p[idx2 + 1] == "."):
                idx1 += 1
                idx2 += 2
            else:
                return False

        return idx1 == len(s) and (idx2 == len(p) or p[idx2] == "*")
            
        
