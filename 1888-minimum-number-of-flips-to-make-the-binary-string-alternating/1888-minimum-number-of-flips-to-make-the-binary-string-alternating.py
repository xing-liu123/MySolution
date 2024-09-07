class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 0

        dp = [[0, 0] for _ in range(n)]

        if s[0] == '1':
            dp[0][0] = 1
        else:
            dp[0][1] = 1

        for i in range(1, n):
            if s[i] == '1':
                dp[i][0] += dp[i - 1][1] + 1
                dp[i][1] = dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
                
        res = sys.maxsize

        for i in range(n):
            
            p1 = dp[-1][0]
            
            p2 = dp[-1][1]

            if (n - 1 - i) % 2 == 0:
                p1 -= dp[i][0]
                p2 -= dp[i][1]
            else:
                p1 -= dp[i][1]
                p2 -= dp[i][0]

            if i % 2 == 0:
                p1 += dp[i][1]
                p2 += dp[i][0]
            else:
                p1 += dp[i][0]
                p2 += dp[i][1]

            res = min(res, p1, p2)

        return res

        