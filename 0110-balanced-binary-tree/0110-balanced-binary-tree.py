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
        
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        
        left = self.getHeight(root.left) if root.left else 0
        right = self.getHeight(root.right) if root.right else 0
        
        return abs(left - right) <= 1
    
    def getHeight(self, root) -> int:
        if not root:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1