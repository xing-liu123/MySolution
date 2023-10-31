class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
            
        probs = [0.0] * (n + 1)
        probs[0] = 1.0
        sum = 1.0
        res = 0.0

        for i in range(1, n + 1):
            probs[i] = sum / maxPts
            if i < k:
                sum += probs[i]
            else:
                res += probs[i]

            if i - maxPts >= 0:
                sum -= probs[i - maxPts]
        
        return res
