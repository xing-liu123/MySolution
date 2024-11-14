# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        res = 0

        def traverse(curr):
            nonlocal res
            if not curr.left and not curr.right:
                return

            if curr.left:
                if not curr.left.left and not curr.left.right:
                    res += curr.left.val
                else:
                    traverse(curr.left)

            if curr.right:
                traverse(curr.right)

        traverse(root)

        return res