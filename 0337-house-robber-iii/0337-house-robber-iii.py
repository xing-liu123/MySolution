# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        nodes = dict()
        return self.traverse(root, nodes)
    
    def traverse(self, curr, nodes) -> int:
        if not curr:
            return 0            
        
        if curr in nodes:
            return nodes[curr]
        
        val1 = curr.val
        
        if curr.left:
            val1 += self.traverse(curr.left.left, nodes) + self.traverse(curr.left.right, nodes)
            
        if curr.right:
            val1 += self.traverse(curr.right.left, nodes) + self.traverse(curr.right.right, nodes)
        
        val2 = self.traverse(curr.left, nodes) + self.traverse(curr.right, nodes)
        
        nodes[curr] = max(val1, val2)
        
        return max(val1, val2)