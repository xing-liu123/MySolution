# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         node = TreeNode(val)
        
#         if not root:
#             return node
        
#         curr = root
        
#         while True:
#             if curr.val > val:
#                 if curr.left:
#                     curr = curr.left
#                 else:
#                     curr.left = node
#                     break
#             elif curr.val < val:
#                 if curr.right:
#                     curr = curr.right
#                 else:
#                     curr.right = node
#                     break
            
#         return root
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
            