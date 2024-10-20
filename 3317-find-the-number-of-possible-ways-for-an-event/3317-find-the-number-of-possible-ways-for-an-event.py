class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        mod = 10 ** 9 + 7
        res = 0

        dp = [[0] * (x + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(1 + n):
            for j in range(1, min(n, x) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] * j) % mod

        for s in range(1, min(n, x) + 1):
            if n >= s:
                res += math.perm(x, s) * dp[n][s] * pow(y, s, mod)
       
        return res % mod