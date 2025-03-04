class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""

        for i in range(min(len(str1), len(str2))):
            sub = str1[:i + 1]

            if len(str1) % len(sub) == 0 and len(str2) % len(sub) == 0:
                len1 = len(str1) // len(sub)
                len2 = len(str2) // len(sub)
                if str1 == sub * len1 and str2 == sub * len2:
                    res = sub

        return res