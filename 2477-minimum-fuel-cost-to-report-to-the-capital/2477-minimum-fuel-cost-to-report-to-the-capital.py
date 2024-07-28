class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)

        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        total_cost = 0

        def dfs(curr) -> int:
            curr_cost = 0
            curr_people = 1
            visited.add(curr)

            for next_city in graph[curr]:
                if next_city not in visited:
                    cost, people = dfs(next_city)
                    curr_cost += cost + (people - 1) // seats + 1
                    curr_people += people

            return curr_cost, curr_people

        return dfs(0)[0]
