class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def canDetonate(bomb1, bomb2) -> bool:
                x1, y1, r1 = bomb1
                x2, y2, r2 = bomb2

                return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if canDetonate(bombs[i], bombs[j]):
                    graph[i].append(j)

        max_num = 0
        visited = set()

        def dfs(curr) -> int:
            visited.add(curr)
            count = 1

            for next_bomb in graph[curr]:
                if not next_bomb in visited:
                    count += dfs(next_bomb)
            
            return count


        for i in range(len(bombs)):
            visited = set()
            
            max_num = max(max_num, dfs(i))

        return max_num
                

                