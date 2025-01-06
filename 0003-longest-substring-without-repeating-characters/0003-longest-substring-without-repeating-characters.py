class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_counts = defaultdict(int)
        longest = 0
        left = 0

        for right in range(n):
            char_counts[s[right]] += 1

            while char_counts[s[right]] > 1:
                char_counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
        


        
