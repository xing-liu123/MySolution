class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, p in flights:
            graph[u].append((v, p))
        
        min_heap = [(0, src, 0)]
        price_map = dict()
        price_map[src] = (0, 0)

        while min_heap:
            cost, city, stop = heapq.heappop(min_heap)
            if city == dst and stop - 1 <= k:
                return cost

            if stop > k:
                continue

            for next_city, next_cost in graph[city]:
                if not next_city in price_map:
                    heapq.heappush(min_heap, (cost + next_cost, next_city, stop + 1))
                    price_map[next_city] = (cost + next_cost, stop + 1)
                else:
                    p, s = price_map[next_city]
                    if cost + next_cost < p or stop + 1 < s:
                        heapq.heappush(min_heap, (cost + next_cost, next_city, stop + 1))
                        price_map[next_city] = (cost + next_cost, stop + 1)

                    
        return -1
