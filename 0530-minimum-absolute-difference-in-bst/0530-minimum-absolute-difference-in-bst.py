# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = sys.maxsize
        
        prevVal = None

        def traverse(curr):
            nonlocal minDiff, prevVal
            if not curr:
                return

            traverse(curr.left)

            if prevVal is not None:
                minDiff = min(curr.val - prevVal, minDiff)
            
            prevVal = curr.val

            traverse(curr.right)

        traverse(root)

        return minDiff