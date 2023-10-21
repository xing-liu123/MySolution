class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = []

        for stone in stones:
            heapq.heappush(queue, -stone)
        
        while len(queue) > 1:
            s1 = -heapq.heappop(queue)
            s2 = -heapq.heappop(queue)

            if s1 != s2:
                heapq.heappush(queue, -abs(s1 - s2))
        
        return -queue[0] if len(queue) == 1 else 0