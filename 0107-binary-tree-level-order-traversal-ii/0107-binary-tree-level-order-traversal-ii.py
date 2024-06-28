from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def traverse(node, level):
            if not node:
                return
            
            if len(res) < level + 1:
                res.append([])
            
            res[level].append(node.val)
            
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
            
        traverse(root, 0)
        
        res.reverse()
        
        return res
        
            