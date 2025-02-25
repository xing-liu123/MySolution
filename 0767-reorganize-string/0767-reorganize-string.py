import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s) # Counts the frequency of each character

        maxHeap = [(-freq, char) for char, freq in counter.items()]

        heapq.heapify(maxHeap)

        lastChar = None

        res = [""] * len(s)
        currIdx = 0

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)

            res[currIdx] = char
            currIdx += 1

            if lastChar:
                heapq.heappush(maxHeap, lastChar)
                lastChar = None

            freq += 1
            if freq < 0:
                lastChar = (freq, char)

        if lastChar:
            return ""

        return "".join(res)

