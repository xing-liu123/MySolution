class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        pointSet = set()

        for x, y, r in circles:
            top = y + r
            bot = y - r
            dx = 0

            print(top, bot)

            for row in range(bot, y + 1):
                for col in range(x - dx, x + dx + 1):
                    pointSet.add((col, row))
                dx += 1

            dx = 0
            for row in range(top, y, -1):
                for col in range(x - dx, x + dx + 1):
                    pointSet.add((col, row))
                dx += 1

        return len(pointSet)
