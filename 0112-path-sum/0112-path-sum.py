# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(curr, currSum):
            if not curr:
                return False

            currSum += curr.val

            if not curr.left and not curr.right:
                if currSum == targetSum:
                    return True

            if curr.left and traverse(curr.left, currSum):
                return True

            if curr.right and traverse(curr.right, currSum):
                return True

            return False

        return traverse(root, 0)
            