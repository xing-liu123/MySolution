# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumOfLeft(root, 0, False)
    
    def sumOfLeft(self, curr, currSum, isLeft) -> int:
        if not curr:
            return 0
        
        if not curr.left and not curr.right:
            if isLeft:
                return curr.val
            else:
                return 0
        
        left = self.sumOfLeft(curr.left, currSum, True) if curr.left else 0
            
        right = self.sumOfLeft(curr.right, currSum, False) if curr.right else 0
        
        return left + right