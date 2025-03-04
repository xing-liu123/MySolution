class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # res = ""

        # for i in range(min(len(str1), len(str2))):
        #     if len(str1) % (i + 1) == 0 and len(str2) % (i + 1) == 0:
        #         sub = str1[:i + 1]
        #         len1 = len(str1) // len(sub)
        #         len2 = len(str2) // len(sub)
        #         if str1 == sub * len1 and str2 == sub * len2:
        #             res = sub

        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)

        gcd_len = gcd(len(str1), len(str2))

        return str1[:gcd_len]