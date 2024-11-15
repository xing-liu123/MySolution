# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        currVal = None

        def traverse(curr):
            nonlocal currVal
            if not curr:
                return True
            
            if not traverse(curr.left):
                return False

            if not currVal is None and curr.val <= currVal:
                return False

            currVal = curr.val

            if not traverse(curr.right):
                return False

            return True

        return traverse(root)