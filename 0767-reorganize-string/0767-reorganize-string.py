class Solution:
    def reorganizeString(self, s: str) -> str:
        charCounts = defaultdict(int)

        for c in s:
            charCounts[c] += 1

        maxHeap = [(-count, char) for char, count in charCounts.items()]

        heapq.heapify(maxHeap)
        res = ""
        temp = None

        while maxHeap:
            
            count, char = heapq.heappop(maxHeap)

            res += char
            count += 1

            if temp:
                heapq.heappush(maxHeap, temp)

            if count < 0:
                if not maxHeap:
                    return ""

                temp = (count, char)
            else:
                temp = None
        

        if temp:
            return ""

            # count, char = heapq.heappop(maxHeap)
            
            # if len(res) > 0 and res[-1] == char:
            #     if maxHeap:
            #         nextCount, nextChar = heapq.heappop(maxHeap)
            #         res += nextChar
            #         nextCount += 1

            #         if nextCount < 0:
            #             heapq.heappush(maxHeap, (nextCount, nextChar))
            #         heapq.heappush(maxHeap, (count, char))
            #     else:
            #         return ""

            # else:
            #     res += char
            #     count += 1

            #     if count < 0:
            #         heapq.heappush(maxHeap, (count, char))

        return res
            

