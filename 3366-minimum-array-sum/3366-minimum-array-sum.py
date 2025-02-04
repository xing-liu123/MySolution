class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        # dp[i][j][l] represents minimum sum up to index i using j op1 operations and l op2 operations
        dp = [[[float('inf')] * (op2 + 1) for _ in range(op1 + 1)] for _ in range(n)]
        
        # Initialize for first element
        dp[0][0][0] = nums[0]  # No operations
        if op1 > 0:
            dp[0][1][0] = (nums[0] + 1) // 2  # Apply op1
        if op2 > 0 and nums[0] >= k:
            dp[0][0][1] = nums[0] - k  # Apply op2
        if op1 > 0 and op2 > 0 and nums[0] >= k:
            # Apply both operations - need to try both orders
            val1 = ((nums[0] - k) + 1) // 2  # op2 then op1
            val2 = ((nums[0] + 1) // 2) - k if (nums[0] + 1) // 2 >= k else float('inf')  # op1 then op2
            dp[0][1][1] = min(val1, val2)
        
        # Process rest of the array
        for i in range(1, n):
            for j in range(op1 + 1):
                for l in range(op2 + 1):
                    # Try not applying any operation
                    if dp[i-1][j][l] != float('inf'):
                        dp[i][j][l] = min(dp[i][j][l], dp[i-1][j][l] + nums[i])
                    
                    # Try applying op1 (division)
                    if j > 0 and dp[i-1][j-1][l] != float('inf'):
                        dp[i][j][l] = min(dp[i][j][l], dp[i-1][j-1][l] + (nums[i] + 1) // 2)
                    
                    # Try applying op2 (subtraction)
                    if l > 0 and nums[i] >= k and dp[i-1][j][l-1] != float('inf'):
                        dp[i][j][l] = min(dp[i][j][l], dp[i-1][j][l-1] + nums[i] - k)
                    
                    # Try applying both operations
                    if j > 0 and l > 0 and nums[i] >= k and dp[i-1][j-1][l-1] != float('inf'):
                        # Try both orders of operations
                        val1 = ((nums[i] - k) + 1) // 2  # op2 then op1
                        val2 = ((nums[i] + 1) // 2) - k if (nums[i] + 1) // 2 >= k else float('inf')  # op1 then op2
                        min_val = min(val1, val2)
                        dp[i][j][l] = min(dp[i][j][l], dp[i-1][j-1][l-1] + min_val)
        
        # Find minimum sum in last row
        result = float('inf')
        for j in range(op1 + 1):
            for l in range(op2 + 1):
                result = min(result, dp[n-1][j][l])
                
        return result



                
                