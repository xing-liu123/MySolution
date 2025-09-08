class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}

        left, maxLen = 0, 0

        for right in range(len(s)):
            char = s[right]
            if char in lastSeen and lastSeen[char] >= left:
                left = lastSeen[char] + 1
            
            lastSeen[char] = right

            maxLen = max(maxLen, right - left + 1)

        return maxLen

        