class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for source, dist, price in flights:
            graph[source].append((dist, price))

        heap = [(0, src, 0)]
        priceAtStop = {}

        while heap:
            totalPrice, curr, stop = heapq.heappop(heap)

            if curr == dst:
                return totalPrice

            if stop > k:
                continue

            for neighbor, price in graph[curr]:
                newPrice = totalPrice + price

                if not (neighbor, stop) in priceAtStop or newPrice < priceAtStop[(neighbor, stop)]:
                    priceAtStop[(neighbor, stop)] = newPrice
                    heapq.heappush(heap, (newPrice, neighbor, stop + 1))

        return -1


