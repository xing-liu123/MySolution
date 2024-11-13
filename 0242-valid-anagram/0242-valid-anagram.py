class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = {}

        for c in s:
            charCount[c] = charCount.get(c, 0) + 1

        for c in t:
            if not c in charCount:
                return False

            if charCount[c] == 0:
                return False

            charCount[c] -= 1

        return True