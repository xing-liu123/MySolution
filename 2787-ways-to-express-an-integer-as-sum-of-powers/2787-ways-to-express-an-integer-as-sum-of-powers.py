MOD = 10 ** 9 + 7
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        seed = []

        curr = 1

        while math.pow(curr, x) <= n:
            seed.append(int(math.pow(curr, x)))
            curr += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for val in seed:
            for i in range(n, val - 1, -1):
                dp[i] = (dp[i] + dp[i - val]) % MOD

        return dp[n]
