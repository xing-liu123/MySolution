class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1
        
        sortedCounts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

        res = ""

        for c, count in sortedCounts.items():
            res += c * count
        
        return res
