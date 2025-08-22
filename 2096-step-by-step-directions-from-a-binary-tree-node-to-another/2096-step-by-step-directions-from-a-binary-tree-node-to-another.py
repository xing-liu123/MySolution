# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        res = ""
        def traverse(curr):
            nonlocal res
            if not curr:
                return (None, "")

            leftChild, leftStr = traverse(curr.left)
            rightChild, rightStr = traverse(curr.right)
            
            if leftChild and rightChild:
                if leftChild.val == startValue:
                    res = "U"*(len(leftStr) + 1) + "R" + (rightStr)
                else:
                    res = "U"*(len(rightStr) + 1) + "L" + (leftStr)
                
                return (None, None)

            elif leftChild:
                if curr.val == startValue: 
                    res = "L" + (leftStr)
                    return (None, None)
                elif curr.val == destValue:
                    res = "U"*(len(leftStr) + 1)
                    return (None, None)
                else:
                    return (leftChild, "L" + leftStr)
                    
            elif rightChild:
                if curr.val == startValue: 
                    res = "R" + (rightStr)
                    return (None, None)
                elif curr.val == destValue:
                    res = "U"*(len(rightStr) + 1)
                    return (None, None)
                else:
                    return (rightChild, "R" + rightStr)
            else:
                if curr.val == startValue or curr.val == destValue:
                    return (curr, "")
                else:
                    return (None, "")

        traverse(root)

        return res