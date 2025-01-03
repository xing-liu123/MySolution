# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0


        while l1 or l2 or carry != 0:
            if not l1 and not l2:
                curr.next = ListNode(carry)
                carry = 0
            elif not l1:
                next_sum = l2.val + carry
                curr.next = ListNode(next_sum % 10)
                carry = next_sum // 10
                curr = curr.next
                l2 = l2.next
            elif not l2:
                next_sum = l1.val + carry
                curr.next = ListNode(next_sum % 10)
                carry = next_sum // 10
                curr = curr.next
                l1 = l1.next
            else:
                next_sum = l1.val + l2.val + carry
                curr.next = ListNode(next_sum % 10)
                carry = next_sum // 10
                curr = curr.next
                l1 = l1.next
                l2 = l2.next

        return dummy.next






            