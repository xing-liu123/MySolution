class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        my_map = defaultdict(lambda: len(wall))

        for row in wall:
            start = 0
            for i in range(len(row) - 1):
                start += row[i]
                my_map[start] -= 1
                

        return min(my_map.values(), default=len(wall))
