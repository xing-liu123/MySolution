class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def dfs(curr):
            visited.add(curr)
            if len(visited) == n:
                return True

            for key in rooms[curr]:
                if not key in visited:
                    if dfs(key):
                        return True
            
            return False

        return dfs(0)