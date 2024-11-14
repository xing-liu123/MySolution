# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(left, right):
            if left > right:
                return None
            
            max_idx = left

            for i in range(left, right + 1):
                if nums[i] > nums[max_idx]:
                    max_idx = i
        
            node = TreeNode(nums[max_idx])
            node.left = buildTree(left, max_idx - 1)
            node.right = buildTree(max_idx + 1, right)
        
            return node

        return buildTree(0, len(nums) - 1)

        