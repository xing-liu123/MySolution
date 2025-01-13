class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = [0] * 26

        for word in words2:
            counts = Counter(word)

            for char in counts.keys():
                idx = ord(char) - ord('a')
                max_freq[idx] = max(max_freq[idx], counts[char])

        res = []

        for word in words1:
            counts = Counter(word)
            isUniversal = True
            for i in range(26):
                char = chr(i + ord("a"))   
                if counts[char] < max_freq[i]:
                    isUniversal = False
                    break
            if isUniversal:
                res.append(word)

        return res