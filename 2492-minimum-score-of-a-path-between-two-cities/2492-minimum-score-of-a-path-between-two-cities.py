class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        minDist = {}
        minDist[1] = sys.maxsize

        queue = deque([(1, sys.maxsize)])

        while queue:
            city, dist = queue.popleft()

            for nextCity, nextDist in graph[city]:
                if not nextCity in minDist or min(dist, nextDist) < minDist[nextCity]:
                    queue.append((nextCity, min(dist, nextDist)))
                    minDist[nextCity] = min(dist, nextDist)
        print(minDist)
        return minDist[n]
        


