class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_counts = defaultdict(int)

        res = 0
        left, right = 0, 0

        while right < len(s):
            c = s[right]

            char_counts[c] += 1

            while char_counts[c] > 1:
                char_counts[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1

        return res