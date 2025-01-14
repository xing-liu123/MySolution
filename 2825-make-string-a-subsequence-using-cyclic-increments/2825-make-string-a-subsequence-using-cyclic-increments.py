class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx1 = idx2 = 0

        while idx1 < len(str1) and idx2 < len(str2):
            if str1[idx1] == str2[idx2] or ord(str1[idx1]) - ord(str2[idx2]) == -1 or str1[idx1] == "z" and str2[idx2] == "a":
                idx2 += 1

            idx1 += 1

        return idx2 == len(str2)
            

