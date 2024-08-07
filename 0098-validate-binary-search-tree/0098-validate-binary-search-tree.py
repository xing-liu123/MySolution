# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         arr = []
#         def traverse(curr) -> bool:
#             if not curr:
#                 return True
            
#             if not traverse(curr.left):
#                 return False
            
#             if len(arr) > 0 and curr.val <= arr[-1]:
#                 return False
            
#             arr.append(curr.val)
            
#             if not traverse(curr.right):
#                 return False
#             else:
#                 return True
        
#         return traverse(root)
        prev = None
        curr = root
        stack = []
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                
                if prev and prev.val >= curr.val:
                    return False
                
                prev = curr
                curr = curr.right
        
        return True
                    