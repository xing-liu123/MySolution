# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        carry = 0

        curr = dummy

        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currSum = val1 + val2 + carry

            currVal = currSum % 10
            carry = currSum // 10

            if l1:
                l1.val = currVal
                curr.next = l1
            elif l2:
                l2.val = currVal
                curr.next = l2
            else:
                curr.next = ListNode(currVal)

            curr = curr.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        return dummy.next
            

            





            