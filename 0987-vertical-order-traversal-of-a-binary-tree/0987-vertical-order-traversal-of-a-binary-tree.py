# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)

        def traverse(curr, curr_row, curr_col):
            if not curr:
                return

            columns[curr_col].append((curr_row, curr.val))
            traverse(curr.left, curr_row + 1, curr_col - 1)

            traverse(curr.right, curr_row + 1, curr_col + 1)

        traverse(root, 0, 0)

        columns = [columns[key] for key in sorted(columns.keys())]
        res = []
        for col in columns:
            res.append([val for _, val in sorted(col)])

        return res

