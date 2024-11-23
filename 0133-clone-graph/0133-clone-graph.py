"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.nodeMap = dict()
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node.val in self.nodeMap:
            return self.nodeMap[node.val]

        newNode = Node(node.val, [])

        self.nodeMap[newNode.val] = newNode

        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(neighbor))

        return newNode