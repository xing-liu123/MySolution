class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        safe = dict()

        def dfs(curr) -> bool:
            if curr in safe:
                return safe[curr]

            safe[curr] = False

            for neighbor in graph[curr]:
                if not dfs(neighbor):
                    return False
                
            safe[curr] = True
            return True
        
        for i in range(len(graph)):  
            if dfs(i):
                res.append(i)
                            
        return res