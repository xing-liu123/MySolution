class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        dp = [[[sys.maxsize] * (op2 + 1) for _ in range((op1 + 1))] for _ in range(n)]

        
        dp[0][0][0] = nums[0]
            
        if op1 > 0:
            dp[0][1][0] = (nums[0] + 1) // 2

        if op2 > 0 and nums[0] >= k:
            dp[0][0][1] = nums[0] - k

        if op1 > 0 and op2 > 0 and nums[0] >= k:
            val1 = (nums[0] + 1) // 2 - k if (nums[0] + 1) // 2 >= k else sys.maxsize
            val2 = (nums[0] + 1 - k) // 2
            dp[0][1][1] = min(val1, val2)

        res = sys.maxsize

        for i in range(1, n):
            for j in range(min(op1 + 1, i + 2)):
                for l in range(min(op2 + 1, i + 2)):
                    if dp[i - 1][j][l] != sys.maxsize:
                        dp[i][j][l] = dp[i - 1][j][l] + nums[i]

                    if j > 0 and dp[i - 1][j - 1][l] != sys.maxsize:
                        dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j - 1][l] + (nums[i] + 1) // 2)

                    if l > 0 and dp[i - 1][j][l - 1] != sys.maxsize and nums[i] >= k:
                        dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l - 1] + (nums[i] - k))

                    if j > 0 and l > 0 and dp[i - 1][j - 1][l - 1] != sys.maxsize and nums[i] >= k:
                        val1 = dp[i - 1][j - 1][l - 1] + (nums[i] - k + 1) // 2
                        val2 = dp[i - 1][j - 1][l - 1] + (nums[i] + 1) // 2 - k if (nums[i] + 1) // 2 >= k else sys.maxsize
                        dp[i][j][l] = min(dp[i][j][l], val1, val2)
  

        for j in range(op1 + 1):
            for l in range(op2 + 1):
                res = min(res, dp[-1][j][l])

        return res



                
                