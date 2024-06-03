# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         currA = headA
#         currB = headB
        
#         while currA and currB:
#             currA = currA.next
#             currB = currB.next
            
#         newA = headA
#         newB = headB
        
#         while currA:
#             currA = currA.next
#             newA = newA.next
            
#         while currB:
#             currB = currB.next
#             newB = newB.next
            
#         while newA != newB:
#             newA = newA.next
#             newB = newB.next
        
#         return newA if newA == newB else None
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            # If pointerA reaches the end of its list, redirect it to headB
            pointerA = pointerA.next if pointerA else headB
            # If pointerB reaches the end of its list, redirect it to headA
            pointerB = pointerB.next if pointerB else headA

        return pointerA  # or pointerB, they are the same at this point
        