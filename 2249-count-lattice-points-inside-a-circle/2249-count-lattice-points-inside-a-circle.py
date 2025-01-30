class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        pointSet = set()

        for x, y, r in circles:
            top = y + r
            bot = y - r
            squaredR = r * r

            for row in range(bot, top + 1):
                 dx = 0

                 while dx ** 2 + (row - y) ** 2 <= squaredR:
                    pointSet.add((x + dx, row))
                    pointSet.add((x - dx, row))
                    dx += 1

        return len(pointSet)
