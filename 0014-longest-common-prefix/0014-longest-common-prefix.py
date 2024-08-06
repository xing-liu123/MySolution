class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        i = 0

        while True:
            for s in strs:
                if len(s) == 0:
                    return ""
                if i == len(s):
                    return res[:i]

                if i == len(res):
                    res += s[i]
                else:
                    if s[i] != res[i]:
                        return res[:i]
            i += 1

        return res