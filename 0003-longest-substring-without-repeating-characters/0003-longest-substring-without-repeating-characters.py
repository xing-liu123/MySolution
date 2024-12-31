class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_counts = defaultdict(int)

        left = 0
        longest = 0

        for right in range(len(s)):
            c = s[right]

            char_counts[c] += 1

            while char_counts[c] > 1:
                c_left = s[left]
                char_counts[c_left] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
