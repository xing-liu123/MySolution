# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.traverse(root)
        return max(dp[0], dp[1])
    
    def traverse(self, curr:Optional[TreeNode]):
        dp = [0] * 2
        if curr == None:
            return dp
            
        leftDp = self.traverse(curr.left)
        rightDp = self.traverse(curr.right)

        dp[0] = max(leftDp[0], leftDp[1]) + max(rightDp[0], rightDp[1])
        dp[1] = leftDp[0] + rightDp[0] + curr.val

        return dp