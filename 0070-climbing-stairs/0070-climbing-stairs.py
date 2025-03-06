class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 1)

        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]
        
        if n == 0 or n == 1:
            return 1

        if n in self.cache:
            return self.cache[n]


        res =  self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = res
        return res