class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        buleGraph = defaultdict(list)

        for u, v in redEdges:
            redGraph[u].append(v)
        
        for u, v in blueEdges:
            buleGraph[u].append(v)

        distances = [[-1] * n for _ in range(2)]
        distances[0][0] = distances[1][0] = 0

        queue = deque([(0, 0), (0, 1)])

        while queue:
            node, color = queue.popleft()
            next_color = 1 - color

            if color == 0:
                for next_node in redGraph[node]:
                    if distances[1][next_node] == -1:
                        distances[1][next_node] = distances[0][node] + 1
                        queue.append((next_node, 1))
            else:
                for next_node in buleGraph[node]:
                    if distances[0][next_node] == -1:
                        distances[0][next_node] = distances[1][node] + 1
                        queue.append((next_node, 0))

        res = []

        for i in range(n):
            if distances[0][i] == -1 and distances[1][i] == -1:
                res.append(-1)
            elif distances[0][i] == -1:
                res.append(distances[1][i])
            elif distances[1][i] == -1:
                res.append(distances[0][i])
            else:
                res.append(min(distances[0][i], distances[1][i]))
        
        return res
                    

