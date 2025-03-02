class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 1)

        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]
        
        if n == 0 or n == 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)