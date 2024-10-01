class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)

        idx1, idx2 = 0, 0
        res = ""

        while idx1 < m and idx2 < n:
            res += word1[idx1] + word2[idx2]
            idx1 += 1
            idx2 += 1

        if idx1 < m:
            res += word1[idx1:]
        
        if idx2 < n:
            res += word2[idx2:]

        return res
