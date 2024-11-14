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

        # queue = deque([root])

        # while queue:
        #     size = len(queue)
        #     level = []

        #     for _ in range(size):
        #         node = queue.popleft()

        #         level.append(node.val)

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)
        #     res.append(level)

        def traverse(curr, level):
            if not curr:
                return
            
            if len(res) == level:
                res.append([])

            res[level].append(curr.val)

            traverse(curr.left, level + 1)
            traverse(curr.right, level + 1)


        traverse(root, 0)

        return res 