class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(colors)

        for u, v in edges:
            if u == v:
                return -1

            graph[u].append(v)

        res = 0

        color_map = {}
        visited = set()
        loop_found = False

        def dfs(curr):
            nonlocal res
            nonlocal loop_found
            color_map[curr] = defaultdict(int)
            visited.add(curr)

            for next_node in graph[curr]:
                
                if next_node in visited:
                    loop_found = True
                    return

                if not next_node in color_map:
                    dfs(next_node)

                for color, count in color_map[next_node].items():
                    color_map[curr][color] = max(color_map[curr][color], count)

            visited.remove(curr)

            color_map[curr][colors[curr]] += 1
            max_count = max(color_map[curr].values())
            res = max(max_count, res)

        for i in range(n):
            if not i in color_map:
                dfs(i)

                if loop_found:
                    return -1
            
        return res
