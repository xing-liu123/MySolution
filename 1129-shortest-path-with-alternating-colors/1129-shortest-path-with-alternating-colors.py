class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        buleGraph = defaultdict(list)

        for u, v in redEdges:
            redGraph[u].append(v)
        
        for u, v in blueEdges:
            buleGraph[u].append(v)

        def bfs(color, answer):
            queue = deque([0])
            answer[0] = 0
            visitedR = set()
            visitedB = set()

            if color == "r":
                visitedB.add(0)
            else:
                visitedR.add(0)

            length = 0

            while queue:
                size = len(queue)
                length += 1
                
                for _ in range(size):
                    curr = queue.popleft()

                    if color == "b":
                        for next_node in buleGraph[curr]:
                            if not next_node in visitedB:
                                visitedB.add(next_node)
                                queue.append(next_node)
                                if answer[next_node] == -1:
                                    answer[next_node] = length
                                    
                    elif color == "r":
                        for next_node in redGraph[curr]:
                            if not next_node in visitedR:
                                visitedR.add(next_node)
                                queue.append(next_node)
                                if answer[next_node] == -1:
                                    answer[next_node] = length
                    
                color = "b" if color == "r" else "r"

        redRes = [-1] * n
        blueRes = [-1] * n

        bfs("r", redRes)
        
        bfs("b", blueRes)

        res = []

        for i in range(n):
            if redRes[i] == -1 and blueRes[i] == -1:
                res.append(-1)
            elif redRes[i] == -1:
                res.append(blueRes[i])
            elif blueRes[i] == -1:
                res.append(redRes[i])
            else:
                res.append(min(redRes[i], blueRes[i]))
        
        return res
                    

