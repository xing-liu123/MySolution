class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        idx = 0

        while True:
            if idx >= len(strs[0]):
                return res
            
            char = strs[0][idx]

            for s in strs:
                if idx >= len(s) or s[idx] != char:
                    return res
            
            idx += 1
            res += char

        return res