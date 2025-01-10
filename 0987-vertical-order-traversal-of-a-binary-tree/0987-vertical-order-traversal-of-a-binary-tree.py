# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        def traverse(curr, row, col):
            if not curr:
                return

            nodes.append((col, row, curr.val))
            traverse(curr.left, row + 1, col - 1)

            traverse(curr.right, row + 1, col + 1)

        traverse(root, 0, 0)

        nodes.sort()

        columns = defaultdict(list)

        for col, row, val in nodes:
            columns[col].append(val)

        return [columns[key] for key in sorted(columns)]

