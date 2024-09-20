class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * (len(s))

        dp[0] = True

        window_sum = 0

        for i in range(1, len(s)):
            if i >= minJump:
                window_sum += dp[i - minJump]

            if i > maxJump:
                window_sum -= dp[i - maxJump - 1]

            if s[i] == '0' and window_sum > 0:
                dp[i] = True

        return dp[-1]