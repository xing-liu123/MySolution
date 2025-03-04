# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDist = 0
        def dfs(curr):
            nonlocal maxDist
            if not curr:
                return 0

            leftDepth = dfs(curr.left)
            rightDepth = dfs(curr.right)

            maxDist = max(maxDist, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)

        dfs(root)
        return maxDist