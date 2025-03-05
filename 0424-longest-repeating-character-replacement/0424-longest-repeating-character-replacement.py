class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26

        maxLen = 0

        left = 0

        for right in range(len(s)):
            counts[ord(s[right]) - ord('A')] += 1

            maxCount = max(counts)


            while right - left + 1 - maxCount > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
                maxCount = max(counts)
                
            maxLen = max(maxLen, right - left + 1)

        return maxLen
            