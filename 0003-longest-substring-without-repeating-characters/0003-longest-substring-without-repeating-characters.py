class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        last_occurence = {}
        longest = 0
        left = 0

        for right in range(n):
            if not s[right] in last_occurence or last_occurence[s[right]] < left:
                last_occurence[s[right]] = right
            else:
                left = last_occurence[s[right]] + 1
                last_occurence[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest
        


        
