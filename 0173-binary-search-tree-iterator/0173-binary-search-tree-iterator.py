# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.array = []

        def traverse(curr):
            if not curr:
                return

            traverse(curr.left)
            self.array.append(curr.val)
            traverse(curr.right)
        traverse(root)
        self.curr_idx = 0

    def next(self) -> int:
        if self.curr_idx >= len(self.array):
            return None
        
        val = self.array[self.curr_idx]
        self.curr_idx += 1
        return val

    def hasNext(self) -> bool:
        return self.curr_idx < len(self.array)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()