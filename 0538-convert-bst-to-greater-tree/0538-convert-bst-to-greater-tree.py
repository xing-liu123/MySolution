# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = 0
        
        def traverse(curr):
            nonlocal currSum
            if not curr:
                return

            traverse(curr.right)
            currSum += curr.val
            curr.val = currSum

            traverse(curr.left)

        traverse(root)
        return root
