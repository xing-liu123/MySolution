# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return ""
        
        res = []

        def traverse(curr, currPath):
            currPath += str(curr.val)

            if not curr.left and not curr.right:
                res.append(currPath)
            
            if curr.left:
                traverse(curr.left, currPath + "->")

            if curr.right:
                traverse(curr.right, currPath + "->")

        traverse(root, "")

        return res