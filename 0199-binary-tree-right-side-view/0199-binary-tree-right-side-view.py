# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        queue = []

        queue.append(root)

        while queue:
            size = len(queue)

            while size > 0:
                node = queue.pop(0)
                if size == 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

                size -= 1
        
        return res