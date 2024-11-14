# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # def traverse(curr):
        #     if not curr:
        #         return

        #     traverse(curr.left)
        #     res.append(curr.val)
        #     traverse(curr.right)

        # traverse(root)

        stack = []

        if not root:
            return res

        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right

        return res