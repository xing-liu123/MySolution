class Solution:
  
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in sorted(tickets):
            graph[u].append(v)

        res = []

        def dfs(curr):
            while graph[curr]:
                next_city = graph[curr].pop(0)
                dfs(next_city)

            res.append(curr)

        dfs("JFK")

        res.reverse()
        return res
             