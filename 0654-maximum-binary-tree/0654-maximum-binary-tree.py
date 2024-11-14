# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def findMaximum(arr):
            max_idx, max_val = 0, arr[0]

            for idx, val in enumerate(arr):
                if val > max_val:
                    max_idx, max_val = idx, val

            return max_idx, max_val
        
        if not nums:
            return None
        
        idx, val = findMaximum(nums)
        
        node = TreeNode(val)

        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])

        return node

        