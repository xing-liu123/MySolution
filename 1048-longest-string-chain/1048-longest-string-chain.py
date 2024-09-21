class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        def isPredecessor(s1, s2):

            idx1, idx2 = 0, 0

            while idx1 < len(s1) and idx2 < len(s2):
                if s1[idx1] == s2[idx2]:
                    idx1 += 1
                idx2 += 1

                if idx2 > idx1 + 1:
                    return False

            return idx1 == len(s1)


        dp = [1] * len(words)

        for i in range(1, len(words)):
            for j in range(i):
                if len(words[i]) == len(words[j]) + 1:
                    if isPredecessor(words[j], words[i]):
                        dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)