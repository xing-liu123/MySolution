from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # graph = defaultdict(list)
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)


        # def dfs(curr) -> int:
        #     visited.add(curr)
        #     height = 0

        #     for next_node in graph[curr]:
        #         if not next_node in visited:
        #             height = max(height, dfs(next_node) + 1)
            
        #     return height

        # res = dict()

        # for i in range(n):
        #     visited = set()
        #     res[i] = dfs(i)

        # min_height = min(res.values())

        # return [i for i in res.keys() if res[i] == min_height]
        if n == 1:
            return [0]
        
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = deque()
        degrees = [0] * n
        for i in range(n):
            degrees[i] = len(graph[i])
            if len(graph[i]) == 1:
                leaves.append(i)
            
        remaining_leaves = n

        while remaining_leaves > 2:
            num_leaves = len(leaves)
            remaining_leaves -= num_leaves

            for _ in range(num_leaves):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
