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

        left = 0
        currCharCount = defaultdict(int)

        def hasAllChars(count1, count2):
            for key in count2.keys():
                if not key in count1 or count1[key] < count2[key]:
                    return False
            
            return True

        for right in range(m):
            currCharCount[s[right]] += 1

            while right - left + 1 >= n and hasAllChars(currCharCount, charCount):
                if right - left + 1 < minWindow:
                    minWindow = right - left + 1
                    res = s[left: right + 1]
                currCharCount[s[left]] -= 1
                left += 1

        return res
                