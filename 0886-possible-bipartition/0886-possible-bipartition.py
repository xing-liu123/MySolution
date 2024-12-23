from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        for person in range(1, n + 1):
            if not person in color:
                color[person] = 1

                queue = deque([person])

                while queue:
                    curr = queue.popleft()

                    for next_person in graph[curr]:
                        if not next_person in color:
                            color[next_person] = -color[curr]
                            queue.append(next_person)
                        elif color[next_person] == color[curr]:
                            return False

        return True
        

        
        