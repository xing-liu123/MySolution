class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_mst = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0

        total = 0

        for _ in range(n):
            u = -1
            best = float('inf')

            for i in range(n):
                if not in_mst[i] and dist[i] < best:
                    best = dist[i]
                    u = i

            in_mst[u] = True
            total += best

            ux, uy = points[u]

            for v in range(n):
                if not in_mst[v]:
                    vx, vy = points[v]
                    d = abs(ux - vx) + abs(uy - vy)
                    if d < dist[v]:
                        dist[v] = d

        return total