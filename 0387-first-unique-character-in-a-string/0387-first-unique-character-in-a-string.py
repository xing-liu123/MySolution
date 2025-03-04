class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCounts = Counter(s)

        for i in range(len(s)):
            if charCounts[s[i]] == 1:
                return i

        return -1