"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.node_map = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head in self.node_map:
            return self.node_map[head]
        
        copy = Node(head.val)
        self.node_map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.copyRandomList(head.random)

        return copy