# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            size = len(queue)
            nodes = []

            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                nodes.append(node.val)

            if len(res) % 2 == 0:
                res.append(nodes)
            else:
                res.append(nodes[::-1])

        return res