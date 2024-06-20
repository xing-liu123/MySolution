from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         res = root.val
        
#         queue = deque([root])
        
#         while queue:
#             size = len(queue)
#             res = queue[0].val
            
#             for _ in range(size):
#                 curr = queue.popleft()
                
#                 if curr.left:
#                     queue.append(curr.left)
                    
#                 if curr.right:
#                     queue.append(curr.right)
        
#         return res
        return self.findLeft(root, 0)[1]

    def findLeft(self, curr, depth) -> (int, int):
        if not curr.left and not curr.right:
            return depth, curr.val
        
                
        leftDepth, leftVal = self.findLeft(curr.left, depth + 1) if curr.left else (-1, 0)
        
        rightDepth, rightVal = self.findLeft(curr.right, depth + 1) if curr.right else (-1, 0)

                
        if leftDepth >= rightDepth:
            return leftDepth, leftVal
        else:
            return rightDepth, rightVal
        
            