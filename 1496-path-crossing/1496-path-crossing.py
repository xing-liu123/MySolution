class Solution:
    def isPathCrossing(self, path: str) -> bool:
        location_set = set()
        location_set.add((0, 0))

        x, y = 0, 0

        for d in path:
            if d == "N":
                y += 1
            elif d == "S":
                y -= 1
            elif d == "E":
                x += 1
            elif d == "W":
                x -= 1

            if (x, y) in location_set:
                return True
            else:
                location_set.add((x, y))

        return False