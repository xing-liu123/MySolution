from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
#         res = []
#         if not root:
#             return res
        
#         queue = deque([root])
        
#         while queue:
#             size = len(queue)
            
#             level = []
            
#             for _ in range(size):
#                 node = queue.popleft()
                
#                 for c in node.children:
#                     queue.append(c)
                
#                 level.append(node.val)
            
#             res.append(level)
        
#         return res
        res = []
        self.order(root, res, 0)
        return res
    
    def order(self, curr: 'Node', res: [], depth: int):
        if not curr:
            return
        
        if len(res) < depth + 1:
            res.append([curr.val])
        else:
            res[depth].append(curr.val)
        
        for c in curr.children:
            self.order(c, res, depth + 1)