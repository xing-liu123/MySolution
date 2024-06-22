# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         currSum = 0
        
#         def convert(curr):
#             nonlocal currSum
#             if not curr: 
#                 return
            
#             convert(curr.right)
#             currSum += curr.val
#             curr.val = currSum
#             convert(curr.left)
            
            
#             return curr
            
#         return convert(root)
        curr = root
        currSum = 0
        stack = []
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                currSum += curr.val
                curr.val = currSum
                
                curr = curr.left
        
        return root