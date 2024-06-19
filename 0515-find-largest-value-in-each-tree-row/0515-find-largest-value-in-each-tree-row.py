from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
        
#         if not root:
#             return res
        
#         queue = deque([root])
        
#         while queue:
            
#             largest = -sys.maxsize - 1
#             size = len(queue)
            
#             for _ in range(size):
#                 node = queue.popleft()
                
#                 if node.left:
#                     queue.append(node.left)
                
#                 if node.right:
#                     queue.append(node.right)
                
#                 if node.val > largest:
#                     largest = node.val
            
#             res.append(largest)
        
#         return res
        res = []
        self.order(res, root, 0)
        return res
        
    def order(self, res: List[int], curr: TreeNode, depth: int):
        if not curr:
            return
        
        if len(res) < depth + 1:
            res.append(curr.val)
        else:
            res[depth] = max(res[depth], curr.val)
        
        self.order(res, curr.left, depth + 1)
        self.order(res, curr.right, depth + 1)
        