# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def arrToBST(left, right) -> TreeNode:
            if left > right:
                return None
            
            mid = left + (right - left + 1) // 2
            root = TreeNode(nums[mid])
            
            root.left = arrToBST(left, mid - 1)
            root.right = arrToBST(mid + 1, right)
            
            return root
            
            
        return arrToBST(0, len(nums) - 1)
    