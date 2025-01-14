# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_map = defaultdict(int)
        res = []
        
        def dfs(cur):
            if not cur:
                return "#"

            arr = f"{cur.val},{dfs(cur.left)},{dfs(cur.right)}"
            
            tree_map[arr] += 1
            if tree_map[arr] == 2: 
                res.append(cur)

            return arr

        dfs(root)

        return res
