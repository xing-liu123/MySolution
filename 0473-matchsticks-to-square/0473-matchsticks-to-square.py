class Solution:
    def __init__(self):
        self.sums = []
        self.target = 0
    
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum = sum(matchsticks)

        if totalSum % 4 != 0:
            return False

        matchsticks.sort(reverse=True)

        self.sums = [0] * 4

        self.target = totalSum//4

        return self.backtracking(matchsticks, 0)

    
    def backtracking(self, matchsticks: List[int], idx: int) -> bool:
        if idx == len(matchsticks):
            return self.sums[0] == self.target and self.sums[1] == self.target and self.sums[2] == self.target

        for i in range(4):
            if self.sums[i] + matchsticks[idx] > self.target:
                continue

            self.sums[i] += matchsticks[idx]
            if self.backtracking(matchsticks, idx + 1):
                return True
            self.sums[i] -= matchsticks[idx]

            if self.sums[i] == 0 or self.sums[i] + matchsticks[idx] == self.target:
                break
            
        return False
        
