# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q) if p.val < root.val else self.lowestCommonAncestor(root.right, p, q)
        right = self.lowestCommonAncestor(root.left, p, q) if q.val < root.val else self.lowestCommonAncestor(root.right, p, q)

        if right and left and (right.val == p.val and left.val == q.val or right.val == q.val and left.val == p.val):
            return root

        if left:
            return left

        if right:
            return right

        return None