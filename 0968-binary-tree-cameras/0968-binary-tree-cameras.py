# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = self.traverse(root)
        if res == 1:
            return self.count + 1
        return self.count

    def traverse(self, curr) -> int:
        if not curr:
            return 2
        
        left = self.traverse(curr.left)
        right = self.traverse(curr.right)

        if left == 2 and right == 2:
            return 1
        
        if left == 1 or right == 1:
            self.count += 1
            return 3

        if left == 3 or right == 3:
            return 2
        