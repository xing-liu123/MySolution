# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(curr, currSum, sumCount):
            nonlocal res

            if not curr:
                return
            
            currSum += curr.val
            res += sumCount[currSum - targetSum]
            sumCount[currSum] += 1
            dfs(curr.left, currSum, sumCount)
            dfs(curr.right, currSum, sumCount)
            sumCount[currSum] -= 1

        sumCount = defaultdict(int)
        sumCount[0] = 1

        if root:
            dfs(root, 0, sumCount)
        
        return res


            