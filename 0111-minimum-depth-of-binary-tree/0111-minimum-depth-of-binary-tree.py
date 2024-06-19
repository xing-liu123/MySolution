# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.depth(root, 1)
    
    def depth(self, node: TreeNode, depth: int) -> int:
        if not node.left and not node.right:
            return depth
        
        left = self.depth(node.left, depth + 1) if node.left else sys.maxsize
        right = self.depth(node.right, depth + 1) if node.right else sys.maxsize
        
        return min(left, right)
        
        
        
       