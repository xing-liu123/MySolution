from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        queue = deque([root])

        while queue:
            size = len(queue)
            
            curr = queue.popleft()
            
            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)


            for _ in range(1, size):
                nextNode = queue.popleft()
                curr.next = nextNode
                curr = nextNode

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

        return root