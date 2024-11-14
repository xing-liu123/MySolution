# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # def traverse(curr):
        #     if not curr:
        #         return
            
        #     traverse(curr.left)
        #     traverse(curr.right)
        #     res.append(curr.val)

        # traverse(root)

        if not root:
            return res

        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.left:
                stack.append(curr.left)
            
            if curr.right:
                stack.append(curr.right)

            res.append(curr.val)

        return res[::-1]