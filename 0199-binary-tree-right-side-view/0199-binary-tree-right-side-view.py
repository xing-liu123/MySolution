from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         if not root:
#             return res
        
#         queue = deque([root])
        
#         while queue:
#             size = len(queue)
            
#             while size > 0:
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
                
#                 if node.right:
#                     queue.append(node.right)
            
#                 if size == 1:
#                     res.append(node.val)
                
#                 size -= 1
        res = []
        self.order(res, root, 0)
        return res
    
    def order(self, res: List[int], curr: TreeNode, depth: int):
        if not curr:
            return
        
        if len(res) < depth + 1:
            res.append(curr.val)
        
        if curr.right:
            self.order(res, curr.right, depth + 1)
        
        if curr.left:
            self.order(res, curr.left, depth + 1)