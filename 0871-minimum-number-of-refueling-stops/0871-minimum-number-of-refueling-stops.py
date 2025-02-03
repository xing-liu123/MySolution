class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        count = 0
        maxHeap = []
        currFuel = startFuel

        for dist, gas in stations:
            while currFuel < dist and maxHeap:
                currFuel -= heapq.heappop(maxHeap)
                count += 1

            if currFuel < dist:
                
                return -1

            heapq.heappush(maxHeap, -gas)

        return count

