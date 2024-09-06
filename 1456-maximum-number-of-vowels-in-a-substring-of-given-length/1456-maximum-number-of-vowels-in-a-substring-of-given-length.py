class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        

        if len(s) < k:
            return 0

        curr = 0
        for c in s[0: k]:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                curr += 1

        res = curr

        for left in range(len(s) - k):
            c1 = s[left + k]
            c2 = s[left]

            if c1 == 'a' or c1 == 'e' or c1 == 'i' or c1 == 'o' or c1 == 'u':
                curr += 1

            if c2 == 'a' or c2 == 'e' or c2 == 'i' or c2 == 'o' or c2 == 'u':
                curr -= 1

            res = max(res, curr)

        return res


