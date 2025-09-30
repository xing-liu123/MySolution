from collections import defaultdict
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        m = n - len(graph)
        oddNodes = []

        for node in graph.keys():
            if len(graph[node]) % 2 == 1:
                oddNodes.append(node)

            if len(oddNodes) > 4:
                return False

        if len(oddNodes) == 0:
            return True

        if len(oddNodes) == 1 or len(oddNodes) == 3:
            return False

        if len(oddNodes) == 2:
            if oddNodes[0] not in graph[oddNodes[1]]:
                return True
            elif m > 0:
                return True
            elif len(graph[oddNodes[0]].union(graph[oddNodes[1]])) < n:
                return True
            else:
                return False

        if len(oddNodes) == 4:
            if oddNodes[0] not in graph[oddNodes[1]] and oddNodes[2] not in graph[oddNodes[3]]:
                return True
            elif oddNodes[0] not in graph[oddNodes[2]] and oddNodes[1] not in graph[oddNodes[3]]:
                return True
            elif oddNodes[0] not in graph[oddNodes[3]] and oddNodes[1] not in graph[oddNodes[2]]:
                return True
 
        return False

        