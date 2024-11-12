# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0

        currA = headA
        
        while currA:
            currA = currA.next
            lengthA += 1

        lengthB = 0
        currB = headB

        while currB:
            currB = currB.next
            lengthB += 1

        currA, currB = headA, headB

        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                currA = currA.next

        elif lengthB > lengthA:
            for i in range(lengthB - lengthA):
                currB = currB.next

        while currA and currB:
            if currA == currB:
                return currA
            
            currA = currA.next
            currB = currB.next

        return None
        
        