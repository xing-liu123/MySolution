class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n + 1) for _ in range(m + 1)]

        for str in strs:
            countOne = str.count('1')
            countZero = str.count('0')
            for i in range(m, countZero - 1, -1):
                for j in range(n, countOne - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - countZero][j - countOne] + 1)
        
        return dp[m][n]