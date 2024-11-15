# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(curr, currSum):
            if not curr:
                return currSum

            currSum = traverse(curr.right, currSum)
            currSum += curr.val
            curr.val = currSum

            currSum = traverse(curr.left, currSum)

            return currSum

        traverse(root, 0)
        return root
