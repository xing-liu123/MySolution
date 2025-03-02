"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
node_map = {}
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head in node_map:
            return node_map[head]

        nodeCopy = Node(head.val)
        node_map[head] = nodeCopy

        nodeCopy.next = self.copyRandomList(head.next)
        nodeCopy.random = self.copyRandomList(head.random)

        return nodeCopy