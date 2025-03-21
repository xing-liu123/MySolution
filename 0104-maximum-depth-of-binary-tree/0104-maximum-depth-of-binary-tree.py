from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        # queue = deque([root])

        # while queue:
        #     depth += 1

        #     size = len(queue)

        #     for _ in range(size):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)

        def traverse(curr, currDepth):
            nonlocal depth
            if not curr:
                return

            depth = max(currDepth, depth)

            traverse(curr.left, currDepth + 1)
            traverse(curr.right, currDepth + 1)

        traverse(root, 1)

        return depth