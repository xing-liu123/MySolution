class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        res = 0
        left, right = 0, 0

        while right < len(s):
            c = s[right]

            while c in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(c)
            res = max(res, right - left + 1)
            right += 1

        return res