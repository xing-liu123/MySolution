class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        return "".join(sorted(list(s), key=lambda x: (counts[x], x), reverse=True))