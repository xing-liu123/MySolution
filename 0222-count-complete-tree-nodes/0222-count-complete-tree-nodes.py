# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.count(root)
    
    def count(self, node) -> int:
        if not node:
            return 0
        
        left = self.count(node.left) if node.left else 0
        right = self.count(node.right) if node.right else 0
        
        return left + right + 1