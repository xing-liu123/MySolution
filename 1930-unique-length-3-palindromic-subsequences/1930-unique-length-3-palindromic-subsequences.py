class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = defaultdict(lambda: 0)
        left[s[0]] = 1

        right = defaultdict(lambda: 0)
        res = set()

        for char in s[1:]:
            right[char] += 1

        for char in s[1:]:
            right[char] -= 1
            for c in left.keys():
                if left[c] > 0 and right[c] > 0:
                    word = c + char + c
                    if not word in res:
                        res.add(word)
            left[char] += 1
        
        return len(res)

