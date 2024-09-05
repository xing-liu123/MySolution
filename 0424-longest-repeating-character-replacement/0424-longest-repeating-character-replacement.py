class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26

        left = 0
        max_count = 0
        res = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord("A")

            arr[idx] += 1

            if arr[idx] > max_count:
                max_count = arr[idx]

            while right - left + 1 - max_count > k:
                arr[ord(s[left]) - ord("A")] -= 1

                left += 1

            res = max(res, right - left + 1)

        return res



            


