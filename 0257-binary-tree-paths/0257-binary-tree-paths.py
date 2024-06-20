# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res
        
        self.traverse(root, res, "")
        
        return res
    
    def traverse(self, curr, res, strs):        
        if not curr.left and not curr.right:
            res.append(strs + str(curr.val))
            return
        
        if curr.left:
            self.traverse(curr.left, res, strs + str(curr.val) + "->")
        
        if curr.right:
            self.traverse(curr.right, res, strs + str(curr.val) + "->")
                