class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        idx1, idx2 = 0, 0

        merged = [""] * (m + n)

        while idx1 < m or idx2 < n:
            if idx1 == m:
                merged[m + idx2] = word2[idx2]
                idx2 += 1
            elif idx2 == n:
                merged[n + idx1] = word1[idx1]
                idx1 += 1
            elif idx1 == idx2:
                merged[idx1 + idx2] = word1[idx1]
                idx1 += 1
            else:
                merged[idx1 + idx2] = word2[idx2]
                idx2 += 1
        
        return ''.join(merged)
