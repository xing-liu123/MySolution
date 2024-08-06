class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx1, idx2, len1, len2 = 0, 0, len(s), len(t)

        while idx1 < len1 and idx2 < len2:
            if s[idx1] != t[idx2]:
                idx2 += 1
            else:
                while idx1 < len1 and idx2 < len2 and s[idx1] == t[idx2]:
                    idx1 += 1
                    idx2 += 1

        return idx1 == len1
