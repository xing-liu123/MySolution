class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorCount = {}
        ballColor = {}

        res = []

        for ball, color in queries:
            if not ball in ballColor:
                ballColor[ball] = color
            
                if not color in colorCount:
                    colorCount[color] = 1
                else:
                    colorCount[color] += 1
            else:
                oldColor = ballColor[ball]
                ballColor[ball] = color

                if not color in colorCount:
                    colorCount[color] = 1
                else:
                    colorCount[color] += 1

                colorCount[oldColor] -= 1

                if colorCount[oldColor] == 0:
                    del colorCount[oldColor]

            res.append(len(colorCount))

        return res