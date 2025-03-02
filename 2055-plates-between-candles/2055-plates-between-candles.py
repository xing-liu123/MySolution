class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preCandle = [-1] * n
        postCandle = [n] * n
        plateCounts = [0] * n
        currentPlate = 0

        lastCandleIdx = -1
        for i in range(n):
            if s[i] == "|":
                lastCandleIdx = i
            else:
                currentPlate += 1
            
            preCandle[i] = lastCandleIdx
            plateCounts[i] = currentPlate


        lastCandleIdx = n

        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                lastCandleIdx = i

            postCandle[i] = lastCandleIdx

        

        res = []

        for left, right in queries:
            leftCandle = postCandle[left]
            rightCandle = preCandle[right]

            if rightCandle > leftCandle:
                res.append(plateCounts[rightCandle] - plateCounts[leftCandle])
            else:
                res.append(0)

        return res