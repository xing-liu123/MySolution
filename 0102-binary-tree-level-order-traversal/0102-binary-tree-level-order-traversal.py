from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            
            level = []
            
            while size > 0:
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                size -= 1
                
                level.append(node.val)
            
            res.append(level)
        
        return res
                
