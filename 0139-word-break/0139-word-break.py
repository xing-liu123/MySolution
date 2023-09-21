class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s))

        for i in range(0, len(s)):
            for word in wordDict:
                if word == s[0 : i + 1] or i >= len(word) and word == s[i - len(word) + 1 : i + 1] and dp[i - len(word)]:
                    dp[i] = True

        return dp[-1]