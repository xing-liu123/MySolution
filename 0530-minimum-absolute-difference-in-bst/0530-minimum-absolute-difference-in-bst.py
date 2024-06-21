# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = sys.maxsize
        prev = None
        
        def traverse(curr):
            nonlocal min_diff, prev
            if not curr:
                return
            
            traverse(curr.left)
            
            if prev and abs(prev.val - curr.val) < min_diff:
                min_diff = abs(prev.val - curr.val)
                
            prev = curr
            
            traverse(curr.right)
                
        traverse(root)
        
        return min_diff
        