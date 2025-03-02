from heapq import heappush, heappop
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        # maxHeap = []

        # for char, count in counts.items():
        #     heappush(maxHeap, (-count, char))

        # res = ""

        # while maxHeap:
        #     count, char = heappop(maxHeap)

        #     res += char * (-count)

        # return res
        maxFreq = max(counts.values())

        buckets = [[] for _ in range(maxFreq + 1)]

        for char, count in counts.items():
            buckets[count].append(char)

        res = ""

        for i in range(maxFreq, 0, -1):
            for char in buckets[i]:
                res += char * i

        return res