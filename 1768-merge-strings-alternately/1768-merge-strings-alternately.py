class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        idx1, idx2 = 0, 0

        merged = []

        while idx1 < m or idx2 < n:
            if idx1 == m:
                merged.append(word2[idx2])
                idx2 += 1
            elif idx2 == n:
                merged.append(word1[idx1])
                idx1 += 1
            elif idx1 == idx2:
                merged.append(word1[idx1])
                idx1 += 1
            else:
                merged.append(word2[idx2])
                idx2 += 1
        
        return ''.join(merged)
