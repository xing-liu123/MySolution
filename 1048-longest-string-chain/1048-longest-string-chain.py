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


        dp = {}
        max_chain_length = 1

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            max_chain_length = max(max_chain_length, dp[word])

        return max_chain_length