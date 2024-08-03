class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1], reverse=True)


        graph = defaultdict(list)
        
        for u, v in tickets:
            graph[u].append(v)

        res = []

        def dfs(curr):
            while graph[curr]:
                dfs(graph[curr].pop())

            res.append(curr)

        dfs("JFK")

        res = reversed(res)

        return res
    
    