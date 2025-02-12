class Solution:
    def longestPalindrome(self, s: str) -> str:

        # n = len(s)

        # def expand(left, right):
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         left -= 1
        #         right += 1

        #     return right - left - 1, left + 1, right - 1

        # maxLen, maxLeft, maxRight = 1, 0, 0

        # for i in range(n):
        #     oddLen, oddLeft, oddRight = expand(i, i)

        #     if oddLen > maxLen:
        #         maxLen, maxLeft, maxRight = oddLen, oddLeft, oddRight

        #     evenLen, evenLeft, evenRight = expand(i, i + 1)

        #     if evenLen > maxLen:
        #         maxLen, maxLeft, maxRight = evenLen, evenLeft, evenRight

        # return s[maxLeft: maxRight + 1]

        # n = len(s)

        # dp = [[False] * n for _ in range(n)]

        # for i in range(n):
        #     dp[i][i] = True

        # left, right = 0, 0

        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             if i + 1 == j or dp[i + 1][j - 1]:
        #                 dp[i][j] = True

        #                 if j - i > right - left:
        #                     left, right = i, j

        # return s[left: right + 1]


        # n = len(s)
        # dp = [[False] * n for _ in range(n)]

        # maxLen = 1
        # res = s[0]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n, 1):
        #         if s[i] == s[j]:
        #             if j - i <= 1 or dp[i + 1][j - 1]:
        #                 dp[i][j] = True

        #                 if j - i + 1 > maxLen:
        #                     maxLen = j - i + 1
        #                     res = s[i: j + 1]          

        # return res
        n = len(s)
        dp = [[False] * n for _ in range(n) ] # dp[i][j] denotes if s[i: j + 1] is palindrome

        for i in range(n):
            dp[i][i] = True

        maxLen = 1
        res = s[0]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j == i + 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if j - i + 1 > maxLen:
                            maxLen = j - i + 1
                            res = s[i: j + 1]

        return res





            



        