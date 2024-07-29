from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color_map = dict()

        queue = deque()
        
        for i in range(len(graph)):
            if i not in color_map:
                color_map[i] = 0
                queue.append(i)

                while queue:
                    size = len(queue)

                    for _ in range(size):
                        node = queue.popleft()
                        color = color_map[node]
                        next_color = 1 - color

                        for next_node in graph[node]:
                            if next_node not in color_map:
                                queue.append(next_node)
                                color_map[next_node] = next_color
                            elif color_map[next_node] == color:
                                return False
                
        return True

        