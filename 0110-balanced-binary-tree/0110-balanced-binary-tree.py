# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        def findDepth(curr):
            if not curr:
                return 0
            
            leftDepth = findDepth(curr.left)
            rightDepth = findDepth(curr.right)

            if leftDepth == -1 or rightDepth == -1:
                return -1
            elif abs(leftDepth - rightDepth) > 1:
                return -1
            else:
                return max(leftDepth, rightDepth) + 1

        return findDepth(root) != -1
            