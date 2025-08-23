class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = {}

        for word in words:
            counter[word] = counter.get(word, 0) + 1
        res = 0
        used = set()
        singleNotUsed = True

        for word, count in counter.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    res += 2 * count
                elif singleNotUsed:
                    res += 2 * count
                    singleNotUsed = False
                else:
                    res += 2 * (count - 1)
            elif word not in used:
                mirror = word[::-1]
                if mirror in counter:
                    used.add(mirror)
                    res += 4 * min(count, counter[mirror])
        
        return res
