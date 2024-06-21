# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = sys.maxsize
        arr = []
        
        def traverse(curr):
            nonlocal min_diff
            if not curr:
                return
            
            traverse(curr.left)
            
            arr.append(curr.val)
            
            if len(arr) >= 2 and abs(arr[-1] - arr[-2]) < min_diff:
                min_diff = abs(arr[-1] - arr[-2])
            
            traverse(curr.right)
                
        traverse(root)
        
        return min_diff
        