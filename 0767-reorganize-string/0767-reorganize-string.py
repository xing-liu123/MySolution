import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # # O(N), where N is the length of s
        # counter = Counter(s) # Counts the frequency of each character

        # # O(M), where M is the number of unique characters
        # maxHeap = [(-freq, char) for char, freq in counter.items()] 

        # # O(M), where M is the number of unique characters. Downheap operation.
        # heapq.heapify(maxHeap)

        # lastChar = None # Use it to hold the lastest appended character to avoid the same character being ajacent

        # res = ""

        # # Nlog(M), there are at most M elements in the heap, pop taks log(M), and we need pop at most N times.
        # while maxHeap:
        #     freq, char = heapq.heappop(maxHeap)

        #     res += char
            
        #     # Put the character back to the heap after one iteraton
        #     if lastChar:
        #         heapq.heappush(maxHeap, lastChar)
        #         lastChar = None

        #     freq += 1
        #     # Store it in lastChar to avoid being ajacent
        #     if freq < 0:
        #         lastChar = (freq, char)

        # # If there are characters leftover, it is impossible to rerange.
        # if lastChar:
        #     return ""

        # # Overall runtime, O(Nlog(M)), Space complexity: O(M) for counter and O(M) for heap, where M is number of unique characters
        # return res
        freqCounts = Counter(s)

        if max(freqCounts.values()) > (len(s) + 1) // 2:
            return ""

        sortedCounts = sorted(freqCounts.items(), key=lambda x: x[1], reverse=True)

        res = [""] * len(s)

        idx = 0

        for char, freq in sortedCounts:
            for _ in range(freq):
                res[idx] = char
                idx += 2

                if idx >= len(res):
                    idx = 1

        return "".join(res)


        

