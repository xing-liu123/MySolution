from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 1

        queue = deque([(root, 1)])

        while queue:
            size = len(queue)

            left = 0
            right = 0

            for i in range(size):
                node, pos = queue.popleft()

                if i == 0:
                    left = pos
                elif i == size - 1:
                    right = pos

                
                if node.left:
                    queue.append((node.left, (pos - 1) * 2 + 1))

                if node.right:
                    queue.append((node.right, (pos - 1) * 2 + 2))
            max_width = max(max_width, right - left + 1)

        return max_width
                