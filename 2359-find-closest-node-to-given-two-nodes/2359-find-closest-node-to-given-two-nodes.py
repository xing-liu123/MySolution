class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        visited1 = dict()

        def dfs(curr, visited, dist):
            visited[curr] = dist
            
            if not edges[curr] in visited and edges[curr] != -1:
                dfs(edges[curr], visited, dist + 1)
        
        dfs(node1, visited1, 0)
        visited2 = dict()
        dfs(node2, visited2, 0)

        print(visited1)
        print(visited2)
        curr_min = sys.maxsize
        res = -1

        for node, dist in visited1.items():
            if node in visited2:
                max_of_two = max(dist, visited2[node])
                if max_of_two < curr_min:
                    res = node
                    curr_min = max_of_two
                elif max_of_two == curr_min and res and node < res:
                    res = node

        return res

