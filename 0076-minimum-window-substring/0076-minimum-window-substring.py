from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        res = ""
        minWindow = float('inf')

        if m < n:
            return res

        charCount = defaultdict(int)

        for c in t:
            charCount[c] += 1

        need = len(charCount)

        left = 0
        currCharCount = defaultdict(int)
        formed = 0

        for right, c in enumerate(s):
            currCharCount[c] += 1

            if c in charCount and currCharCount[c] == charCount[c]:
                formed += 1

            while need == formed:
                if right - left + 1 < minWindow:
                    minWindow = right - left + 1
                    res = s[left: right + 1]

                deleteC = s[left]
                currCharCount[deleteC] -= 1
                if deleteC in charCount and currCharCount[deleteC] < charCount[deleteC]:
                    formed -= 1
                left += 1

        return res
                