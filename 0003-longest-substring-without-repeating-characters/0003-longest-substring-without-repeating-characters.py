class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        left = 0
        maxLen = 0

        for right, c in enumerate(s):
            if c in lastSeen and lastSeen[c] >= left:
                left = lastSeen[c] + 1

            lastSeen[c] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen 
        


        
