class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        
        for key in graph:
            graph[key].sort(reverse=True)
            
        res = []
        
        
        
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            
            res.append(airport)
        
        dfs("JFK")
        
        res.reverse()
        
        return res
    
    