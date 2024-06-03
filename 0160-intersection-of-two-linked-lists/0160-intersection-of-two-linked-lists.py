# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        
        while currA and currB:
            currA = currA.next
            currB = currB.next
            
        newA = headA
        newB = headB
        
        
        while currA:
            currA = currA.next
            newA = newA.next
            
        while currB:
            currB = currB.next
            newB = newB.next
            
        while newA != newB:
            newA = newA.next
            newB = newB.next
        
        return newA if newA == newB else null
        