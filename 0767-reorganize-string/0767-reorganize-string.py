from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)

        max_heap = [(-count, char) for char, count in char_counts.items()]
        heapify(max_heap)

        res = ""
        last_char = None

        while max_heap:
            count, char = heappop(max_heap)

            res += char
            count += 1

            if last_char:
                heappush(max_heap, last_char)
                last_char = None

            if count < 0:
                last_char = (count, char)

        return res if not last_char else ""


        
            

