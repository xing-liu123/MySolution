class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        lastSeen = {}
        maxLen = 0
        left = 0

        for right in range(n):
            if s[right] in lastSeen:
                left = lastSeen[s[right]] + 1
            lastSeen[s[right]] = right

            maxLen = max(maxLen, right - left + 1)

        return maxLen

            
        


        
