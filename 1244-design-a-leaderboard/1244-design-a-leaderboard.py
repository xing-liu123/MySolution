from bisect import bisect_left, insort
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.counts = {}
        self.keys = []

    def updateCount(self, score, delta):
        if delta == 0:
            return
        count = self.counts.get(score, 0) + delta
        if count == 0:
            del self.counts[score]
            i = bisect_left(self.keys, score)
            if i < len(self.keys) and self.keys[i] == score:
                self.keys.pop(i)
        else:
            if score not in self.counts:
                insort(self.keys, score)
            self.counts[score] = count


    def addScore(self, playerId: int, score: int) -> None:
        old = self.scores.get(playerId, 0)

        if old != 0:
            self.updateCount(old, -1)

        self.scores[playerId] = old + score

        self.updateCount(old + score, 1)

    def top(self, K: int) -> int:
        res, need = 0, K

        for score in reversed(self.keys):
            if need == 0:
                break
            
            count = self.counts[score]
            if need > count:
                res += count * score
                need -= count
            else:
                res += need * score
                need = 0

        return res

    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        del self.scores[playerId]
        self.updateCount(score, -1)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)