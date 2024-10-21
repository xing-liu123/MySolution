"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        currP = p
        parents_p = set()
        parents_p.add(p.val)
        
        currQ = q
        parents_q = set()
        parents_q.add(q.val)

        while currP.parent or currQ.parent:
            if currP.parent:
                currP = currP.parent

                if currP.val in parents_q:
                    return currP

                parents_p.add(currP.val)
            
            if currQ.parent:
                currQ = currQ.parent
                if currQ.val in parents_p:
                    return currQ

                parents_q.add(currQ.val)

        return NULL
            

