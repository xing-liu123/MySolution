from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root:
            return res
        
        queue = deque([root])
        
        while queue:
            
            largest = -sys.maxsize - 1
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                if node.val > largest:
                    largest = node.val
            
            res.append(largest)
        
        return res