# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(curr):
            if not curr:
                return [0, 0]
            dp = [0] * 2
            
            left = helper(curr.left)
            right = helper(curr.right)

            dp[0] = max(left[0], left[1]) + max(right[0], right[1])
            dp[1] = left[0] + right[0] + curr.val

            return dp

        dp = helper(root)
        return max(dp[0], dp[1])