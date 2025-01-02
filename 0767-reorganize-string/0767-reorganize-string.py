import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = defaultdict(int)

        for c in s:
            char_counts[c] += 1

        max_heap = [(-count, char) for char, count in char_counts.items()]

        heapq.heapify(max_heap)

        res = []
        last_char = None

        while max_heap:
            count, char = heapq.heappop(max_heap)

            res.append(char)

            count += 1

            if last_char:
                heapq.heappush(max_heap, last_char)
                last_char = None

            if count < 0:
                last_char = (count, char)

        if last_char:
            return ""

        return ''.join(res)
                
        

        
            

