class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
                    max_len = max(max_len, dp[i + 1][j + 1])
        
        return max_len