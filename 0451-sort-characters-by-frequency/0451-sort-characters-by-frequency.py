from heapq import heappush, heappop
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        maxHeap = []

        for char, count in counts.items():
            heappush(maxHeap, (-count, char))

        res = ""

        while maxHeap:
            count, char = heappop(maxHeap)

            res += char * (-count)

        return res