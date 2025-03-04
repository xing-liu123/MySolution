class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        charCount = [0] * 26

        for c in s:
            charCount[ord(c) - ord('a')] += 1
        
        for c in t:
            charCount[ord(c) - ord('a')] -= 1

            if charCount[ord(c) - ord('a')] < 0:
                return False

        return True
